<?php
/**
 * 使用PHP近似实现AOP
 * @author cyy0523xc@gmail.com
 */

/** 
 * 基类
 * @author cyy0523xc@gmail.com
 */
class CyyBase
{
    public function before()
    {
        echo "before\n";
    }

    public function after()
    {
        echo "after\n";
    }
}

/** 
 * 业务类
 * @author cyy0523xc@gmail.com
 */
class CyyControl extends CyyBase
{
    public function foobar()
    {
        echo '业务逻辑', "\n";
    }

    public function before()
    {
        parent::before();
        echo "child class before\n";
    }
}


/** 
 * 业务逻辑类的包装类
 * @author cyy0523xc@gmail.com
 */
final class AOP
{
    private $instance;

    public function __construct($instance)
    {
        $this->instance = $instance;
    }

    public function __call($method, $params)
    {
        if (!$this->__methodExists($method)) {
            throw new Exception("Call undefinded method " . get_class($this->instance) . "::$method");
        }

        // 调用前置函数
        if ($this->__methodExists('before')) {
            $this->__callMethod('before');
        }

        // 调用业务函数
        $return = $this->__callMethod($method, $params);

        // 调用后置函数
        if ($this->__methodExists('after')) {
            $this->__callMethod('after');
        }
        
        return $return;
    }

    /**
     * 判断方法是否存在
     * 使用双下划线前缀主要是为了避免冲突
     * @param string $method 方法名
     * @return mixed
     */
    private function __methodExists($method)
    {
        return method_exists($this->instance, $method);
    }

    /**
     * 调用方法
     * @param string $method 方法名
     * @param array  $params 参数数组
     * @return mixed
     */
    private function __callMethod($method, array $params = null)
    {
        $callBack = array(
            $this->instance,
            $method
        );

        if (null === $params) {
            return call_user_func($callBack);
        } else {
            return call_user_func_array($callBack, $params);
        }
    }
}

/** 
 * 工厂方法
 *
 */
class Factory
{
    public function getInstance($class_name)
    {
        return new AOP(new $class_name());
    }
}

//客户端调用演示
try {
    $obj = Factory::getInstance('CyyControl');
    $obj->foobar();
} catch(Exception $e) {
    echo 'Caught exception: ', $e->getMessage();
}
