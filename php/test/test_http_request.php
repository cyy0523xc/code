<?php
require '../init.php';

L('cai_http_request');

$url = 'http://www.youmi.net/';

var_dump(CaiHttpRequest::get($url));