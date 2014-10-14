<?php
/**
 * 将markdown文件中的表格转化为对应的sql语句
 * 表格格式：http://git.ibbd.net/ibbd/ibbd-bc-py/blob/master/doc/db-tables.md 
 *
 * @example

### table中文说明：tablename

desc....

字段       | 类型        | 其他属性 | 说明
---        | ---         | ---      | ---
fieldname1 | varchar(50) | index    | 该字段的说明

 *
 * @author Alex <cyy0523xc@gmail.com>
 * @copyright IBBD
 * @see 
 * @todo 组合索引，前缀索引
 * @version 20141014
 */

//***************  config begin  **************

// 匹配tablename，md文件中如：## 用户登陆表：user_login （user_login就是tablename）
define('PATTORN_TABLE_NAME',     '/^##+.*(:|：)(?P<tablename>(data|user|log)_[a-z_]+)\s*$/');

// 表格字段开始的标志，格式如：---- | ------ | -----| ------ 
define('PATTORN_TABLE_BEGIN',    '/^\-+\s*\|\s*\-+\s*\|\s*\-+/');

// 匹配表格的注释，如匹配tablename中的“用户登陆表”
define('PATTORN_TABLE_COMMENT',  '/^##+\s*(?P<comment>.*?)(:|：)/');

// 字段属性是否默认加上: NOT NULL
define('DEFAULT_NOT_NULL',       true);

// md格式文件地址
$md_file = 'db-tables.md';

// sql代码的保存地址
$create_sql_file = 'ibbd_bc_create_table.sql';

//***************  config end  **************

// 读入md格式的文件
$lines = file($md_file);

// 表名
$table_name = '';

// 是否已经进入了表的字段
$table_field_begin = false;

// sql语句
$table_sql = array();

// sql字段开始标志
$sql_field_begin = false;

// 表的注释
$table_comment = '';

// 索引
$indexs = array();

// 循环处理每行数据
foreach ($lines as $line) {
    $line = trim($line);
    if ('' === $table_name) {
        // 检查数据表开始的位置 
        $table_name = getTableName($line);

        // 表的注释
        if (!empty($table_name)) { 
            if (1 === preg_match(PATTORN_TABLE_COMMENT, $line, $matchs)) {
                $table_comment = trim($matchs['comment']);
            } else {
                $table_comment = '';
            }
        }
    } else {
        if (false === $table_field_begin) {
            // 检查字段开始的位置
            $table_field_begin = checkTableFieldBegin($line);

            // 如果是数据表开始的位置
            if (true === $table_field_begin) {
                $table_sql[$table_name] = "\nCREATE TABLE `{$table_name}` {";
            }
        } else {
            if ('' === $line) {

                // 处理索引
                if (!empty($indexs)) {
                    $index_sql = implode(",\n", $indexs);
                    $table_sql[$table_name] .= ",\n{$index_sql}";
                } 

                // 给sql加上结束标识
                $table_sql[$table_name] .= "\n} ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='{$table_comment}';\n";

                // 字段结束，重置标识
                $table_field_begin    = false;
                $table_name           = '';
                $sql_field_begin      = false;
                $indexs               = array();
            } else {
                // 如果不是第一次进入的话，需要在前一个语句上加逗号
                if (true === $sql_field_begin) {
                    $table_sql[$table_name] .= ',';
                } else {
                    $sql_field_begin = true;
                }

                // 生成sql语句
                $arr = explode('|', $line);

                // 解释内容
                $field_name    = trim($arr[0]);
                $field_name    = str_replace("\\", '', $field_name);
                $field_type    = strtoupper(trim($arr[1]));
                $field_comment = trim($arr[3]);

                // 自增和主键
                $ext = array();
                DEFAULT_NOT_NULL && $ext[] = 'NOT NULL';
                $arr[2] = trim($arr[2]);
                if (!empty($arr[2])) {
                    // 处理额外属性
                    $arr[2]  = strtoupper($arr[2]); 
                    $ext_arr = explode(',', $arr[2]);
                    foreach ($ext_arr as $attr) {
                        $attr = trim($attr);
                        $attr = str_replace("\\", '', $attr);
                        switch ($attr) {
                        case "PRIMARY":
                            $ext[] = 'PRIMARY KEY';
                            break;
                        case 'UNIQUE':
                            $ext[] = 'UNIQUE KEY';
                            break;
                        case 'AUTO_INCREMENT':
                            $ext[] = 'AUTO_INCREMENT';
                            break;
                        case 'INDEX':
                            $indexs[] = "    INDEX (`{$field_name}`)";
                            break;
                        default:
                            if ('DEFAULT' === substr($attr, 0, 7)) {
                                $ext[] = $attr;
                            }
                            break;
                        } // end of switch
                    } // end of foreach
                } // end of if

                $ext = empty($ext) ? '' : implode(' ', $ext);

                // sql语句
                $table_sql[$table_name] .= "\n    `{$field_name}` {$field_type} {$ext} COMMENT '{$field_comment}'";
            }
        }
    }
} // end of foreach

// 组成最后的sql文件的内容
$sql  = "# md文件：http://git.ibbd.net/ibbd/ibbd-bc-py/blob/master/doc/db-tables.md\n";
$sql .= "# Create By http://git.ibbd.net/ibbd/ibbd-bc-py/blob/master/doc/md-table2sql.php\n";
$sql .= "# Create At " . date("Y-m-d H:i:s") . "\n\n\n";
$sql .= implode("", $table_sql);

// 写入文件
echo $sql;
file_put_contents($create_sql_file, $sql);


// ******************** 以下是函数 ***********************

// 获取tablename
function getTableName($line) 
{
    if (1 === preg_match(PATTORN_TABLE_NAME, $line, $matchs)) {
        return $matchs['tablename'];
    }

    return '';
}

// 判断是否为字段的开始位置
function checkTableFieldBegin($line) {
    if (1 === preg_match(PATTORN_TABLE_BEGIN, $line)) {
        return true;
    }
    return false;
}
