<?php
/**
 * 初始化入口
 * @author cyy0523xc@gmail.com
 * @version $Id$
 */
date_default_timezone_set("Asia/Shanghai");



define('CAI_ROOT_PATH', dirname(__FILE__) . '/'); //根目录

require CAI_ROOT_PATH . 'config/constant.php';
require CAI_CONFIG_PATH . 'config.php';

//公共函数库
require CAI_LIB_PATH . 'cai_functions.php';

//基础类库
require CAI_LIB_PATH . 'cai_base.php';
require CAI_LIB_PATH . 'cai_err_msg.php';
