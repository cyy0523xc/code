<?php
/**
 * 错误信息
 * @author cyy0523xc@gmail.com
 *
 */
!defined('CAI_ROOT_PATH') && exit('Access Deny!');

class CaiErrMsg extends CaiBase
{
    /**
     * 错误信息
     * @var string
     */
    private static $msg = array();

    /**
     * 设置异常信息
     * @param string $msg 错误信息
     * @param int $code 错误代码
     * @return void
     */
    public static function set($msg, $code = 0)
    {
        self::$msg[] = array(
            $code => $msg
        );
    }

    /**
     * 获取异常信息函数
     * @return array
     */
    public static function get()
    {
        return self::$msg;
    }
}
