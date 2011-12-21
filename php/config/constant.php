<?php
/**
 * 公共常量定义，这是第一个要引用的文件
 * 注：
 * 1，目录常量字符串最后一个字符统一为"/"。
 *
 * @author cyy0523xc@gmail.com
 * @version $Id$
 */
//目录常量
define('CAI_LIB_PATH',    CAI_ROOT_PATH . 'lib/');      //基础类库及函数库目录
define('CAI_MODULE_PATH', CAI_ROOT_PATH . 'module/');   //平台类库及应用类库目录
define('CAI_CONFIG_PATH', CAI_ROOT_PATH . 'config/');   //配置目录
define('CAI_DATA_PATH',   CAI_ROOT_PATH . 'tmp/data/'); //公共数据目录
define('CAI_CACHE_PATH',  CAI_ROOT_PATH . 'tmp/cache/');//cache目录
define('CAI_LOG_PATH',    CAI_ROOT_PATH . 'tmp/log/');  //log目录