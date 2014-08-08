module Fluent
  class OutputFieldsParser < Fluent::Output
    Fluent::Plugin.register_output('fields_parser', self)

    # config_param定义的参数对应配置文件的参数
    config_param :remove_tag_prefix,  :string, :default => nil
    config_param :add_tag_prefix,     :string, :default => nil
    config_param :parse_key,          :string, :default => 'message'
    config_param :fields_key,         :string, :default => nil
    config_param :pattern,            :string,
                 :default => %{([a-zA-Z_]\\w*)=((['"]).*?(\\3)|[\\w.@$%/+-]*)}  # field="value.."

    def compiled_pattern
      @compiled_pattern ||= Regexp.new(pattern)
    end

    # 这个应该是入口函数
    # @param tag 
    # @param es 
    def emit(tag, es, chain)
      tag = update_tag(tag)
      es.each { |time, record|
        Engine.emit(tag, time, parse_fields(record))
      }
      chain.next
    end

    def update_tag(tag)
      if remove_tag_prefix
        if remove_tag_prefix == tag
          tag = ''
        elsif tag.to_s.start_with?(remove_tag_prefix+'.')
          tag = tag[remove_tag_prefix.length+1 .. -1]
        end
      end
      if add_tag_prefix
        tag = tag && tag.length > 0 ? "#{add_tag_prefix}.#{tag}" : add_tag_prefix
      end
      return tag
    end

    def parse_fields(record)
      source = record[parse_key].to_s
      target = fields_key ? (record[fields_key] ||= {}) : record

      source.scan(compiled_pattern) do |match|
        (key, value, begining_quote, ending_quote) = match
        next if key.nil?
        next if target.has_key?(key)
        value = value.to_s
        from_pos = begining_quote.to_s.length
        to_pos = value.length - ending_quote.to_s.length - 1
        target[key] = value[from_pos..to_pos]
      end
      return record
    end
  end
end
