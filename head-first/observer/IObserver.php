<?php
/** 
 * @author Alex <cyy0523xc@gmail.com>
 * @copyright IBBD.net
 * @see 
 * @todo 
 * @version 2015-06-30
 */
namespace Observer;

//require_once './ObservableInterface.php';

//use Observer\ObservableInterface;

interface IObserver {

    /**
     * 观察者接受更新数据接口
     * @param ObservableInterface $observable 可观察对象
     */
    public function update(IObservable $observable);
}
