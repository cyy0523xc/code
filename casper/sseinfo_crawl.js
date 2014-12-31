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
            selector: '#r3 a[rel="2"]'
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
        } // end of company_list
    }
};



//************************* 以下是主体流程 *********************

var casper = require('casper').create(page_task.browser);
var IBBD = require('libs/ibbd.js').create();

casper.start();

// 任务
IBBD.task.init();
IBBD.task.add(page_task);
IBBD.task.process();

casper.run(function() {
    this.echo('任务完成');
    var data = IBBD.getData();
    for (var key in data) {
        this.echo(key);
        //require('utils').dump(data[key]);
    }
    this.exit();
});
