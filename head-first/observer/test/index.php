<?php
/** 
 * @author Alex <cyy0523xc@gmail.com>
 * @copyright IBBD.net
 * @see 
 * @todo 
 * @version 2015-07-01
 */
require "./News.php";
require "./User.php";
require "./User2.php";

use News\News;
use News\User;
use News\User2;

$news = new News();
$user = new User();

$news->register($user);
$news->addNews('author1', 'this is the first news.');

// 加入新的观察者
$user2 = new User2();
$news->register($user2);
$news->addNews('author2', 'this is the second news.');

$news->remove($user);
$news->addNews('author3', 'this is the 3rd news.');

