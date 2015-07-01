<?php
/** 
 * @author Alex <cyy0523xc@gmail.com>
 * @copyright IBBD.net
 * @see 
 * @todo 
 * @version 2015-06-30
 */
namespace News;

require_once "../ObservableInterface.php";
require_once "../ObserverInterface.php";
require_once "./NewsInterface.php";

use Observer\ObservableInterface;
use Observer\ObserverInterface;
use News\NewsInterface;

class News implements ObservableInterface, NewsInterface {

    /**
     * 观察者列表
     */
    private $observer_list = array();

    /**
     * 数据是否发生了该表
     * 该值为true时，才会触发通知观察者
     */
    private $is_change = false;

    private $author = '';
    private $news = '';


    /**
     * 注册观察者
     * @param ObserverInterface $observer
     */
    public function register(ObserverInterface $observer) 
    {
        $class_name = get_class($observer);
        $this->observer_list[$class_name] = $observer;
        echo "\nregister: ", $class_name;
    }

    /**
     * 移除观察者
     * @param ObserverInterface $observer
     */
    public function remove(ObserverInterface $observer)
    {
        $class_name = get_class($observer);
        if (isset($this->observer_list[$class_name])) {
            unset($this->observer_list[$class_name]);
            echo "\nremove: ", $class_name;
        }
    }

    /**
     * 设置通知阀值
     */
    public function setChanged()
    {
        $this->is_change = true;
    }

    /**
     * 通知观察者 
     */
    public function notify()
    {
        if (true !== $this->is_change) {
            return;
        }

        foreach ($this->observer_list as $observer) {
            $observer->update($this);
        }

        $this->is_change = false;
        echo "\nnotify all.";
    }

    public function addNews($author, $news)
    {
        $this->author = $author;
        $this->news = $news;

        $this->setChanged();
        $this->notify();
    }

    public function getAuthor() 
    {
        return $this->author;
    }

    public function getNews()
    {
        return $this->news;
    }

}
