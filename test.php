<?php
echo phpinfo();

/**
 * 
 * @param unknown_type $a
 */
function test ($a)
{
    echo $a;
    return $a;
}

class A
{

    private $a = 'aa';

    function test ($a)
    {
        $this->a = $a;
    }
}