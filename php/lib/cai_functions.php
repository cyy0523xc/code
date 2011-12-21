<?php
/**
 * 独立函数库
 * @author cyy0523xc@gmail.com
 * 
 */

!defined('CAI_ROOT_PATH') && exit('Access Deny!');

/**
 * Load: 加载模块
 * @param string $name 模块名，例如cai_db
 */
function L ($module)
{
    $type = substr($module, 0, 4);
    if ('cai_' == $type)
    {
        require_once CAI_LIB_PATH . $module . '.php';
    }
    else if ('caim' == $type)
    {
        require_once  CAI_MODULE_PATH . $module . '.php';
    }
}

/**
 * Load Array: 加载多个模块
 * @param array $array 模块名，例如array('cai_db')
 */
function LA (array $array)
{
    foreach ($array as $module)
    {
        $type = substr($module, 0, 4);
        if ('cai_' == $type)
        {
            require_once YM_CM_LIB_PATH . $module . '.php';
        }
        else if ('caim' == $type)
        {
            require_once  YM_CM_MODULE_PATH . $module . '.php';
        }
    }
}

/**
 * 对file_get_contents的封装
 * @param string $url URL|filename
 * @param int $timeout
 * @return string The read data or false for failure
 */
function fileGetContents ($url, $timeout = 1)
{
    $ctx = stream_context_create(array(
    'http' => array('timeout' => $timeout)
    ));

    return @file_get_contents($url, 0, $ctx);
}

/**
 * 获取真实IP
 * @param  void
 * @return string ip
 */
function getIp ()
{
    if (isset($_SERVER))
    {
        if (isset($_SERVER["HTTP_X_FORWARDED_FOR"]))
        {
            $realip = $_SERVER["HTTP_X_FORWARDED_FOR"];
            //如果是多个地址组成的字符串
            if (0 < ($pos = strpos($realip, ',')))
            {
                $realip = substr($realip, 0, $pos);
            }
        }
        elseif (isset($_SERVER["HTTP_CLIENT_IP"]))
        {
            $realip = $_SERVER["HTTP_CLIENT_IP"];
        }
        else
        {
            $realip = $_SERVER["REMOTE_ADDR"];
        }
    }
    else
    {
        if (getenv('HTTP_X_FORWARDED_FOR'))
        {
            $realip = getenv('HTTP_X_FORWARDED_FOR');
            //如果是多个地址组成的字符串
            if (0 < ($pos = strpos($realip, ',')))
            {
                $realip = substr($realip, 0, $pos);
            }
        }
        elseif (getenv('HTTP_CLIENT_IP'))
        {
            $realip = getenv('HTTP_CLIENT_IP');
        }
        else
        {
            $realip = getenv('REMOTE_ADDR');
        }
    }

    //如果是局域网ip的话，则返回握手协议中的ip
    if (isLocalIp($realip))
    {
        return YM_LOCAL_IP;
    }

    return $realip;
}

/**
 * 获取IP
 * @return string ip
 */
function getRemoteAddrIp ()
{
    if (isset($_SERVER))
    {
        $ip = $_SERVER["REMOTE_ADDR"];
    }
    else
    {
        $ip = getenv('REMOTE_ADDR');
    }

    //把局域网ip都设置成唯一的ip
    if (isLocalIp($ip))
    {
        return '192.168.0.1';
    }

    return $ip;
}

/**
 * 判断ip是否是局域网ip
 * @param $dotip string
 * @return boolean
 */
function isLocalIp ($ip)
{
    if ('127.0.0.1' == $ip)
    {
        return true;
    }

    $ip = explode('.', $ip);
    if (10 == $ip[0])
    {
        return true;
    }
    elseif (172 == $ip[0] && $ip[1] > 15 && $ip[1] < 32)
    {
        return true;
    }
    elseif (192 == $ip[0] && 168 == $ip[1])
    {
        return true;
    }

    return false;
}

/**
 * 获取长整型的ip(默认返回本机ip的长整型)
 * @param $ip    string    ip地址
 * @return long
 */
function getLongIp ($ip = '')
{
    empty($ip) && $ip = getIp();
    $ip = ip2long($ip);
    //为兼容32和64位系统，做的修改
    if ($ip < 0)
    {
        $ip = (float) sprintf('%u', $ip);
    }

    return $ip;
}

/**
 * 判断事件是否以p%的概率发生
 * @param int $p 概率(0~100)
 * @return boolean
 **/
function getProbability ($p)
{
    return mt_rand(0, 99) < $p;
}

/**
 * 解析url中的参数字符串
 * @param string $str 字符串
 * @return arrray
 */
function parseQueryString ($str)
{
    $op = array();
    $pairs = explode("&", $str);
    foreach ($pairs as $pair)
    {
        @list ($k, $v) = array_map("rawurldecode", explode("=", $pair));
        $op[$k] = $v;
    }
    return $op;
}

/**
 * 把数组拼接成URL参数的形式（不含urlencode，通常用在写日志的地方）
 * @param array $data 数据
 * @return string
 */
function httpBuildQueryUnencode ($data)
{
    $ret = array();
    foreach ((array) $data as $k => $v)
    {
        array_push($ret, $k . '=' . $v);
    }
    return implode('&', $ret);
}

/**
 * 获取http user aget
 * retunr string
 */
function getUserAgent ()
{
    if (isset($_SERVER["HTTP_X_DEVICE_USER_AGENT"]))
    {
        return $_SERVER["HTTP_X_DEVICE_USER_AGENT"];
    }
    elseif (isset($_SERVER["HTTP_X_ORIGINAL_USER_AGENT"]))
    {
        return $_SERVER["HTTP_X_ORIGINAL_USER_AGENT"];
    }
    elseif (isset($_SERVER["HTTP_X_OPERAMINI_PHONE_UA"]))
    {
        return $_SERVER["HTTP_X_OPERAMINI_PHONE_UA"];
    }
    elseif (isset($_SERVER["HTTP_USER_AGENT"]))
    {
        return $_SERVER["HTTP_USER_AGENT"];
    }

    return '';
}

/**
 * 例如：
 * $arr = array(
 * array('key1' => 'val1', 'key2' => 'val2'),
 * array('key1' => 'val3', 'key2' => 'val4'),
 * );
 * $key = 'key1';
 * 则结果为：
 * array(
 * 'val1' => array('key1' => 'val1', 'key2' => 'val2'),
 * 'val3' => array('key1' => 'val3', 'key2' => 'val4'),
 * );
 *
 * @param array $arr
 * @param string $key
 */
function arrayMapKey(array $arr, $key)
{
    $returns = array();
    if (empty($arr))
    {
        return $returns;
    }

    foreach ($arr as $k)
    {
        $returns[$k[$key]] = $k;
    }

    return $returns;
}