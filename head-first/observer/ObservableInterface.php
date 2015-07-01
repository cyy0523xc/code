<?php
/** 
 * @author Alex <cyy0523xc@gmail.com>
 * @copyright IBBD.net
 * @see 
 * @todo 
 * @version 2015-06-30
 */
namespace Observer;

interface ObservableInterface {

    /**
     * 注册观察者接口
     * @param ObserverInterface $observer 观察者 
     */
    public function register(ObserverInterface $observer);

    /**
     * 移除观察者 
     * @param ObserverInterface $observer 观察者 
     */
    public function remove(ObserverInterface $observer);

    /**
     * 设置通知阀值
     */
    public function setChanged();

    /**
     * 通知观察者
     */
    public function notify();

}
