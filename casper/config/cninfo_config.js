// 深交所互动易：中小企业版

exports.config = {

    // 浏览器配置
    browser: {
    },

    // 页面的URL
    url: 'http://irm.cninfo.com.cn/szse/ssgsList.html',

    // 前置动作
    pre_op: [
        {
            // 点击动作
            type: 'click',
            selector: '#kulist #one2'
        }
    ],

    // 需要抓取的变量
    vars: {
        // 获取表格数据
        'company_list': {
            type:  'list',
            selector: '#con_one_2 li',
            cols: {
                company_logo: {
                    selector: '.headpic img',
                    attr: 'src'
                },

                company_id: {
                    selector: '.code a',
                    as_id: true            // 作为主键
                },

                company_name: {
                    selector: '.name a'
                },

                company_url: {
                    selector: '.headpic a',
                    attr:     'href',                      // 获取属性

                    // 获取该url的详细数据
                    tasks: {
                        as_child_task: false,     // @todo 是否作为独立子任务
                        pre_op: [],
                        vars: {
                            'company_id': {
                                selector: '.zw_banner_box dd *:nth-last-child(1)'
                            },

                            // 直接用父节点的company_name值
                            //'company_name': '@.company_name',

                            //'reply_num': {
                                //selector: 'div.com_info ul li:first-child strong',
                                //type: 'int'
                            //},

                            'follow_num': {
                                selector: '.gzbtn_text',
                                //regexp: /\d+/,
                                type: 'int'
                            }
                        }
                    }
                }
            },

            // 分页数据
            page: {
                num:  2,                 // 最多获取多少页的数据，默认抓取所有数据
                //num:  "#pagination a:nth-last-child(2)",
                next: '#zxPage span[title="Next Page"] a',
                current: '#zxPage span.current',
                delay: 2
            }
        } // end of company_list
    }
};
