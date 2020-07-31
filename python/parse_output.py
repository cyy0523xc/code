'''
将异常输出进行格式化

Author: alex
Created Time: 2020年07月31日 星期五 11时45分58秒
'''
import os
import re


def parse_file(reader):
    """处理一个文件"""
    new_lines = []
    lines = reader.readlines()
    change = False
    for line in lines:
        # return output_json(None, None, code=200, message="查询参数有误：" + str(e))
        matches = re.findall('(.*)return output_json.*\s*\+\s*str\(e\)', line)
        if len(matches) == 0:
            new_lines.append(line)
            continue
        change = True
        new_lines.append('%sprint(str(e))\n' % matches[0])
        line = re.sub('\s*\+\s*str\(e\)', '', line)
        line = line.replace('："', '"')
        new_lines.append(line)

    if change:
        return new_lines
    return None


def parse_filename(filename):
    with open(filename) as r:
        lines = parse_file(r)
    if lines is not None:
        print('parse: ', filename)
        with open(filename, 'w') as w:
            w.writelines(lines)


def parse_dir(path):
    for filename in os.listdir(path):
        if not filename.endswith('.py'):
            continue
        filename = os.path.join(path, filename)
        parse_filename(filename)


if __name__ == '__main__':
    parse_dir('xiaopeng/server/')
