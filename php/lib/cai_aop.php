<?php
/** 
 * AOP逻辑类的包装类
 *
 * 执行顺序：
 * 1. 全局前置函数
 * 2. 局部前置函数
 * 3. 业务逻辑
 * 4. 局部后置函数
 * 5. 全局后置函数
 *
 * @author cyy0523xc@gmail.com
 */
final class CaiAOP
{
    private $instance;

    // 全局的前置函数和后置函数
    // 每个action调用时都会调用
    // @todo 可以在配置文件配置
    const GLOBAL_BEFORE_FUNC = '_before';
    const GLOBAL_AFTER_FUNC  = '_after';

    // 特定action的前置函数和后置函数的前缀
    const LOCAL_BEFORE_PRE   = '_before_';
    const LOCAL_AFTER_PRE    = '_after_';

    public function __construct($instance)
    {
        $this->instance = $instance;
    }

    public function __call($method, $params)
    {
        if (!$this->__hasMethod($method)) {
            throw new Exception("Call undefinded method " . get_class($this->instance) . "::$method");
        }

        // 调用全局前置函数
        if ($this->__hasMethod(AOP::GLOBAL_BEFORE_FUNC)) {
            $this->__callMethod(AOP::GLOBAL_BEFORE_FUNC);
        }

        // 调用前置函数
        if ($this->__hasMethod(AOP::LOCAL_BEFORE_PRE . $method)) {
            $this->__callMethod(AOP::LOCAL_BEFORE_PRE . $method);
        }

        // 调用业务函数
        $return = $this->__callMethod($method, $params);

        // 调用局部后置函数
        if ($this->__hasMethod(AOP::LOCAL_AFTER_PRE . $method)) {
            $this->__callMethod(AOP::LOCAL_AFTER_PRE . $method);
        }

        // 调用全局后置函数
        if ($this->__hasMethod(AOP::GLOBAL_AFTER_FUNC)) {
            $this->__callMethod(AOP::GLOBAL_AFTER_FUNC);
        }
        
        return $return;
    }

    /**
     * 判断方法是否存在
     * 使用双下划线前缀主要是为了避免冲突
     * @param string $method 方法名
     * @return mixed
     */
    private function __hasMethod($method)
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
