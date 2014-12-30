// e互动

var page_task = {

    // 浏览器配置
    browser: {
        verbose: true,
        logLevel: "debug",

        // 浏览器size
        viewportSize: {width: 800, height:1200},

        userAgent: 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/39.0.2171.65 Chrome/39.0.2171.65 Safari/537.36',

        loadImages:  false
    },

    // 页面的URL
    url: 'http://sns.sseinfo.com/list/company.do',

    // 前置动作
    pre_op: [
        {
            // 点击动作
            type: 'click',
            selector: '#nav li a[href="list/company.do"]'
        }
    ],

    // 需要抓取的变量
    vars: {
        // 获取表格数据
        'company_list': {
            type:  'list',
            selector: '#allCompany .companyBox',
            cols: {
                e_uid: {
                    selector: 'a[rel="tag"]',
                    attr: 'uid',           // 这个配置可以不要，默认就是innerText
                    type: 'int'
                },

                company_logo: {
                    selector: 'a[rel="tag"] img',
                    attr: 'src'
                },

                company_id: {
                    col: 1,
                    type: 'int',
                    as_id: true            // 作为主键
                },

                company_name: {
                    col: 2
                },

                company_url: {
                    selector: 'div a:nth-last-child(1)',
                    attr:     'href',                      // 获取属性
                    pre_str:  'http://sns.sseinfo.com/',   // 前缀字符串

                    // 获取该url的详细数据
                    tasks: {
                        as_child_task: false,     // @todo 是否作为独立子任务
                        pre_op: [],
                        vars: {
                            'company_id': {
                                selector: 'div.com_info p',
                                substr: [1, -1],     // [start, len]
                                type: 'int'
                            },

                            // 直接用父节点的company_name值
                            //'company_name': '@.company_name',

                            'reply_num': {
                                selector: 'div.com_info ul li:first-child strong',
                                type: 'int'
                            },

                            'follow_num': {
                                selector: '#followedNum',
                                type: 'int'
                            }
                        }
                    }
                }
            },

            // 分页数据
            page: {
                num:  2,                 // 最多获取多少页的数据，默认抓取所有数据
                //num:  "#pagination a:nth-last-child(2)",
                next: '#pagination .next',
                current: '#pagination span[class="current"]',
                delay: 2
            }
        }
    }
};



//************************* 以下是主体流程 *********************

var casper = require('casper').create(page_task.browser);
var IBBD = require('libs/ibbd.js').create();

casper.start(page_task.url, function() {
    this.echo(this.status(true));
}).then(function() {
    this.scrollToBottom();
});

require('utils').dump(IBBD);

// 前置动作
if (page_task.pre_op.length > 0) {
    IBBD.preOperate(page_task.pre_op);
}

// 解释变量
/*
for (var k in page_task.vars) {
    casper.echo("-------------------------" + k);
    var v = page_task.vars[k];
    if ('object' === typeof v.page) {
        IBBD.processPages(k, v);
    } else {
        IBBD.parse(k, v);
    }
}*/

var key_list = [];
for (var k in page_task.vars) {
    key_list.push(k);
}

var processOneVar = function(params_list) {
    var current_key = params_list.pop();
    var current_val = page_task.vars[current_key];

    casper.echo('开始处理变量：' + current_key);
    if ('object' === typeof current_val.page) {
        IBBD.processPages(current_key, current_val);
    } else {
        IBBD.parse(current_key, current_val);
    }
    casper.echo('结束处理变量：' + current_key);

    if (params_list.length > 0) {
        casper.then(function() {
            processOneVar(params_list);
        });
    } else {
        return;
    }
}

casper.then(function() {
    IBBD.debug(key_list);
    processOneVar(key_list);
});

casper.run(function() {
    this.echo('任务完成');
    var data = IBBD.getData();
    for (var key in data) {
        this.echo(key);
        //require('utils').dump(data[key]);
    }
    this.exit();
});
