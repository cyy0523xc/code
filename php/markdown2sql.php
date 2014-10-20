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
 * @todo 前缀索引
 * @version 20141014
 */

//***************  config begin  **************

// 匹配tablename，md文件中如：## 用户登陆表：user_login （user_login就是tablename）
define('PATTORN_TABLE_NAME',     '/^##+.*(:|：)(?P<tablename>(data|user|log)_[a-z_0-9]+)\s*$/');

// 表格字段开始的标志，格式如：---- | ------ | -----| ------ 
define('PATTORN_TABLE_BEGIN',    '/^\-+\s*\|\s*\-+\s*\|\s*\-+/');

// 匹配表格的注释，如匹配tablename中的“用户登陆表”
define('PATTORN_TABLE_COMMENT',  '/^##+\s*(?P<comment>.*?)(:|：)/');

// 匹配组合索引的类型 
define('PATTORN_EXT_INDEX_TYPE', '/^\*\*(?P<type>index|unique|primary)\*\*/');

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
$sql_field_flag = 0;

// 表的注释
$table_comment = '';

// 索引
$indexs = array();

// 表格是否为空
$table_empty = true;

// 组合索引的类型：primary, unique, index
$ext_index_type = '';

// 数据表的个数
$table_count = 0;

// 循环处理每行数据
$max_line_num = count($lines);
foreach ($lines as $line_no => $line) {
    $line = trim($line);

    if ( (!empty($line) && '#' === $line[0]) 
        || ($line_no === $max_line_num - 1)
    ) {
        if (!empty($table_name)) {
            // 这是上一个数据表的结束
            // 清空所有标识变量
            echo "    Table END.\n\n";

            // 表格不为空才需要处理
            if (false === $table_empty) {
                $table_count++;

                // 处理索引
                if (!empty($indexs)) {
                    $index_sql = implode(",\n", $indexs);
                    $table_sql[$table_name] .= ",\n{$index_sql}";
                } 

                // 给sql加上结束标识
                $table_sql[$table_name] .= "\n) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='{$table_comment}';\n";
            } else {
                // 如果表格为空，则重置为空
                !empty($table_sql[$table_name]) && $table_sql[$table_name] = '';
            }

            // 字段结束，重置标识
            $table_field_begin    = false;
            $table_name           = '';
            $sql_field_flag       = 0;
            $indexs               = array();
            $table_empty          = true;
            $ext_index_type       = '';
        } // end of 上一个表格

        // 检查数据表开始的位置 
        $table_name = getTableName($line);

        // 如果是表格开始的位置
        if (!empty($table_name)) { 
            echo $table_name, " BEGIN:\n";

            // 获取表的注释
            if (1 === preg_match(PATTORN_TABLE_COMMENT, $line, $matchs)) {
                $table_comment = trim($matchs['comment']);
            } else {
                $table_comment = '';
            }
        }
        
    } // end of if # === $line[0]
    elseif (!empty($table_name)) {
        // 进入表格的处理范围 

        // 如果字段还没开始 
        if (0 === $sql_field_flag) {
            // 检查字段开始的位置
            $table_field_begin = checkTableFieldBegin($line);

            // 如果是数据表开始的位置
            if (true === $table_field_begin) {
                $table_sql[$table_name] = "\nCREATE TABLE IF NOT EXISTS `{$table_name}` (";
                $sql_field_flag = 1;
                
                echo "    Field BEGIN\n";
            }
        } elseif (1 === $sql_field_flag) {
            // 正在处理字段
            if (empty($line)) {
                // 如果遇到空行，则表示表格结束
                $sql_field_flag = 2;
                echo "    Field END\n";
            } else {
                // 如果不是空行，则为有效字段

                // 如果不是第一次进入的话，需要在前一个语句上加逗号
                if ($table_empty) {
                    $table_empty = false;
                } else {
                    $table_sql[$table_name] .= ',';
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
            } // end of 字段处理
        } else {
            // 正在处理组合索引
            if (empty($ext_index_type)) {
                if (1 === preg_match(PATTORN_EXT_INDEX_TYPE, $line, $matches)) {
                    $ext_index_type = trim($matches['type']);
                    echo "    process {$ext_index_type}...\n";
                    
                    // 加了一个特殊的前缀：第一次碰到非空行时去掉前缀
                    $ext_index_type = '--' . $ext_index_type;
                }
            } elseif ('--' === substr($ext_index_type, 0, 2)) {
                if ("" === $line) {
                    continue;
                } elseif ('- ' === substr($line, 0, 2)) {
                    // 碰到一个组合索引
                    echo "    type: {$ext_index_type}   line: {$line}\n";
                    $ext_index_type = substr($ext_index_type, 2);
                    $line = trim(substr($line, 2));
                    $table_sql["{$line_no}"] = getExtIndexSql($table_name, $ext_index_type, $line);
                } else {
                    // 碰到非法的非空行
                    echo "[ERROR] line : {$line_no}\n";
                    $ext_index_type = '';
                }
            } else {
                if ('- ' === substr($line, 0, 2)) {
                    // 碰到一个组合索引
                    echo "    line: {$line}\n";
                    $line = trim(substr($line, 2));
                    $table_sql["{$line_no}"] = getExtIndexSql($table_name, $ext_index_type, $line);
                } else {
                    // 碰到空行或者其他不符合规范的行
                    $ext_index_type = '';
                }
            }
        }
    } // end of if !empty($table_name)

} // end of foreach

// 组成最后的sql文件的内容
$sql  = "# md文件：http://git.ibbd.net/ibbd/ibbd-bc-py/blob/master/doc/db-tables.md\n";
$sql .= "# Desc 该生成的sql文档暂不包含前缀索引，请自行添加。\n";
$sql .= "# Create By http://git.ibbd.net/ibbd/ibbd-bc-py/blob/master/doc/markdown2sql.php\n";
$sql .= "# Create At " . date("Y-m-d H:i:s") . "\n";
$sql .= "# 可以在mysql控制台使用souce导入\n";
$sql .= "\n\n";
$sql .= implode("", $table_sql);

// 写入文件
//echo $sql;
file_put_contents($create_sql_file, $sql);
echo "\nAll is OK!\nTables Count: {$table_count}\nSave to file: {$create_sql_file}.\n\n";

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
function checkTableFieldBegin($line) 
{
    if (1 === preg_match(PATTORN_TABLE_BEGIN, $line)) {
        return true;
    }
    return false;
}

// 获取组合索引的sql 
function getExtIndexSql($table_name, $index_type, $line) 
{
    $fields = explode(',', $line);
    $fields = array_map("processFieldName", $fields);

    $sql = "\nALTER TABLE `{$table_name}`";
    switch ($index_type) {
    case 'primary':
        $sql .= " ADD PRIMARY KEY";
        break;
    case 'unique':
        $sql .= " ADD UNIQUE INDEX";
        break;
    case 'index':
        $sql .= " ADD INDEX";
        break;
    default:
        return "";
    }

    $sql .= "(" . implode(',', $fields) . ");\n";
    return $sql;
}

function processFieldName($field_name) 
{
    return "`" . str_replace("\\", '', trim($field_name)) . "`";
}
