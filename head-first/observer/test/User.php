<?php
/** 
 * @author Alex <cyy0523xc@gmail.com>
 * @copyright IBBD.net
 * @see 
 * @todo 
 * @version 2015-07-01
 */
namespace News;

require_once "../IObservable.php";
require_once "../IObserver.php";

use Observer\IObservable;
use Observer\IObserver;

class User implements IObserver {

    public function update(IObservable $observable) 
    {
        $author = $observable->getAuthor();
        $news = $observable->getNews();

        echo "\n update: author=", $author, "  news=", $news;
    }
}
