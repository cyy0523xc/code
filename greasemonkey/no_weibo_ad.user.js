// ==UserScript==
// @name          No Weibo Advertisements
// @namespace     http://cyy0523xc.github.io/
// @description   删除微博的广告等多余信息。基于Cao Weibo修改
// @include       http://www.weibo.com/*
// @include       http://weibo.com/*
// @copyright     2014, cyy0523xc@gmail.com
// ==/UserScript==

// return script name
function script_name()
{
    return "NoWeiboAd";
}

// return debug flag
function debug_flag()
{
    return true;
}

// function return the result of xpath query
function xpath(query)
{
    return document.evaluate(query, document, null, XPathResult.UNORDERED_NODE_SNAPSHOT_TYPE, null);
}

// common function: remove nodes
function remove_nodes(allNode)
{
    var remove_num = 0;
    // for each forward
    for (var i=0; i<allNode.snapshotLength; ++i)
    {
        var thisNode = allNode.snapshotItem(i);
        if (thisNode)
        {
            thisNode.parentNode.removeChild(thisNode);
            remove_num++;
        }
    }

    return remove_num;
}

function remove_xpath(node_path)
{
    var remove_num = remove_nodes(xpath(node_path));
    console.log('Remove xpath = ' + node_path + '    num = ' + remove_num);
}

// function
function remove_ad()
{
    // get '<div>' with attribute 'feedtype="ad"'
    remove_xpath('//div[@feedtype="ad"]');
    
    remove_xpath('//div[@ad-data]');
}

// 
function remove_other()
{
	var id_list = ["trustPagelet_checkin_lotteryv5", "trustPagelet_indexright_recom", "pl_rightmod_ads36", "trustPagelet_recom_memberv5", "pl_leftnav_app" ];
    for (var i in id_list) {
        remove_xpath('//div[@id="' + id_list[i] + '"]');
    }
}

// function
function remove_feed_spread()
{
    // get '<div>' with attribute 'node-type="feed_spread"'
    remove_xpath('//div[@node-type="feed_spread"]');
}

// main function
function main()
{
    if (debug_flag())
    {
        console.log('Starting ' + script_name());
    }
    // remove advertisements
    remove_ad();
    // remove feed spread
    remove_feed_spread();
    // remove other
    remove_other();

    return 0;
}

/////////////////////////////////////////////////////////////////////////////////

window.setTimeout(main, 1000);
