<?php
/** 
 * @author Alex <cyy0523xc@gmail.com>
 * @copyright IBBD.net
 * @see 
 * @todo 
 * @version 2015-07-01
 */
namespace News;

interface INews {

    /**
     * 添加新闻
     * @param string $author 
     * @param string $news 
     */
    public function addNews($author, $news);

    /**
     * 获取作者 
     * @return string
     */
    public function getAuthor();

    /**
     * 获取新闻主体
     * @return string 
     */
    public function getNews();
}

