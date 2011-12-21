<?php
/**
 * 网络请求相关的库函数
 * @author cyy0523xc@gmail.com
 *
 */

!defined('CAI_ROOT_PATH') && exit('Access Deny!');

class CaiHttpRequest extends CaiBase
{
    
    const TIMEOUT = 2;
    
    public static $http_code = 200;
    
    /**
     * 发送请求，post数据
     * @param string $url 完整的请求地址
     * @return array
     */
    public static function post($url, $timeout = self::TIMEOUT)
    {
        $url = parse_url($url);
    
        if (!isset($url['port']))
        {
            if ($url['scheme'] == 'http')
            {
                $url['port'] = 80;
            }
            elseif ($url['scheme'] == 'https')
            {
                $url['port'] = 443;
            }
        }
        $url['query'] = isset($url['query']) ? $url['query'] : '';
        $url['protocol'] = $url['scheme'] . '://';
        $eol = "\r\n";
    
        $headers = array();
        $headers[] = "POST " . $url['protocol'] . $url['host'] . $url['path'] . " HTTP/1.0";
        $headers[] = "Host: " . $url['host'];
        $headers[] = "Referer: " . $url['protocol'] . $url['host'] . $url['path'];
        $headers[] = "Content-Type: application/x-www-form-urlencoded";
        $headers[] = "Content-Length: " . strlen($url['query']) . $eol . $eol . $url['query'];
    
        //test begin
        $headers = array();
        $headers[] = "GET " . $url['protocol'] . $url['host'] . $url['path'] . '?' . $url['query'] . " HTTP/1.0";
        $headers[] = "Host: " . $url['host'];
        $headers[] = "Connection:Close" . $eol . $eol;
        //$headers[] = "Content-Length: " . strlen($url['query']) . $eol . $eol . $url['query'];
    
        //test end
    
        $headers = implode($eol, $headers);
    
        $fp = fsockopen($url['host'], $url['port'], $errno, $errstr, $timeout);
        if ($fp)
        {
            fputs($fp, $headers);
            $result = '';
            while ( !feof($fp) )
            {
                $result .= fgets($fp, 128);
            }
            fclose($fp);
    
            //test
            echo $result, "\n\n\n";
            if (preg_match('/^HTTP.*\s(\d{3,3})\s/', $result, $match))
            {
                self::$http_code = $match[1];
            }
    
            //removes headers
            $pattern = "/^.*\r\n\r\n/s";
            $result = preg_replace($pattern, '', $result);
            return array('code' => 0, 'data' => trim($result));
        }
    
        return array('code' => -1, 'msg' => $errstr);
    }
    
    /**
     * 发送请求，post数据
     * @param string $url 完整的请求地址
     * @return array
     */
    public static function get($url, $timeout = self::TIMEOUT)
    {
        $__url = $url;
        $url = parse_url($url);
    
        if (!isset($url['port']))
        {
            if ($url['scheme'] == 'http')
            {
                $url['port'] = 80;
            }
            elseif ($url['scheme'] == 'https')
            {
                $url['port'] = 443;
            }
        }
        $eol = "\r\n";
    
        $headers = array();
        $headers[] = "GET " . $__url . " HTTP/1.0";
        $headers[] = "Host: " . $url['host'];
        $headers[] = "Connection:Close" . $eol . $eol;
    
        echo $headers = implode($eol, $headers);
        $fp = fsockopen($url['host'], $url['port'], $errno, $errstr, $timeout);
        if ($fp)
        {
            fputs($fp, $headers);
            $result = '';
            while ( !feof($fp) )
            {
                $result .= fgets($fp, 128);
            }
            fclose($fp);
    
            //test
            echo $result, "\n\n\n";
            if (preg_match('/^HTTP.*\s(\d{3,3})\s/', $result, $match))
            {
                self::$http_code = $match[1];
            }
    
            //removes headers
            $pattern = "/^.*\r\n\r\n/s";
            $result = preg_replace($pattern, '', $result);
            return array('code' => 0, 'data' => trim($result));
        }
    
        return array('code' => -1, 'msg' => $errstr);
    }
    
    
}