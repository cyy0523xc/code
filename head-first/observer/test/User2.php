<?php
/** 
 * @author Alex <cyy0523xc@gmail.com>
 * @copyright IBBD.net
 * @see 
 * @todo 
 * @version 2015-07-01
 */
namespace News;

require_once "../ObservableInterface.php";
require_once "../ObserverInterface.php";

use Observer\ObservableInterface;
use Observer\ObserverInterface;

class User2 implements ObserverInterface {

    public function update(ObservableInterface $observable) 
    {
        //$author = $observable->getAuthor();
        $news = $observable->getNews();

        echo "\n update: news=", $news;
    }
}
