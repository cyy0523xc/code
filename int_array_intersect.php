<?php

function int_array_intersect ()
{
    if (func_num_args() < 2)
    {
        trigger_error('param error', E_USER_ERROR);
    }
    
    $args = func_get_args();
    
    foreach ($args as $arg)
    {
        if (! is_array($arg))
        {
            trigger_error('param error', E_USER_ERROR);
        }
    }
    
    $intersect = function  ($a, $b)
    {
        $result = array();
        
        $length_a = count($a);
        $length_b = count($b);
        
        for ($i = 0, $j = 0; $i < $length_a && $j < $length_b; null)
        {
            if ($a[$i] < $b[$j] && ++ $i)
            {
                continue;
            }
            
            if ($a[$i] > $b[$j] && ++ $j)
            {
                continue;
            }
            
            $result[] = $a[$i];
            
            if (isset($a[$next = $i + 1]) && $a[$next] != $a[$i])
            {
                ++ $j;
            }
            ++ $i;
        }
        
        return $result;
    };
    
    $result = array_shift($args);
    sort($result);
    
    foreach ($args as $arg)
    {
        sort($arg);
        $result = $intersect($result, $arg);
    }
    
    return $result;
}

$rand = function() {
    $result = array();

    for ($i = 0; $i < 1000; $i++) {
        $result[] = mt_rand(1, 10000);
    }

    return $result;
};

$param_a = $rand();
$param_b = $rand();

$time = microtime(true);

$result = int_array_intersect($param_a, $param_b);

$time = microtime(true) - $time;

echo "int_array_intersect: {$time}\n";

?>