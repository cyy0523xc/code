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
                    pre_str:  'http://sns.sseinfo.com/'    // 前缀字符串
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



// *********************************************

// 结果保存数组
var data = [];

var IBBD = {
    debug: function(msg) {
        require('utils').dump(msg);
    },

    // @param int sleep_time 单位：毫秒
    sleep: function(sleep_time) {
        var end = Date.now() + sleep_time;
        for (; Date.now() < end;) {}
    },

    getInnerText: function(selector) {
        return document.querySelector(selector).innerText;
    },

    getSelectorInt: function(selector) {
        return parseInt(IBBD.getInnerText(selector), 10);
    },

    format: function(val, config) {
        // 格式化
        val = val.trim();
        if ('string' === typeof config.type) {
            switch (config.type) {
                case 'int':
                    val = parseInt(val, 10);
                break;
                case 'float':
                    val = parseFloat(val);
                break;
            }
        }

        // 字符串替换
        if ('object' === typeof config.replace) {
            val = val.replace(config.replace[0], config.replace[1]);
        }

        // 前缀
        if ('string' === typeof config.pre_str) {
            val = config.pre_str + val;
        }

        return val;
    },

    evaluate: function(config) {
        return casper.evaluate(function(config) {
            var val = document.querySelector(config.selector);
            return val.innerText;
        }, config);
    },

    evaluateSelector: function(selector) {
        return casper.evaluate(function(selector) {
            var val = document.querySelector(selector);
            return val.innerText;
        }, selector);
    },

    pre_op: function(op_list) {
        // 前置动作
        for (var i in op_list) {
            var op = op_list[i];
            switch(op.type) {
                case 'click':
                    casper.waitForSelector(op.selector, function() {
                    this.echo(op.selector);
                    this.click(op.selector);
                });
                break;
            }
        }
    },

    // 当前页码
    current_page: 1,
    have_next_page: true,

    // 解释变量(没有分页的数据)
    parse: function(key, val) {
        casper.waitForSelector(val.selector, function() {
            switch (val.type) {
                case 'table':
                    data[key] = IBBD.table(val);
                    break;

                default:
                    data[key] = IBBD.evaluate(val);
                    data[key] = IBBD.format(data[key], val);
                    break;
            }
            this.echo("========================" + key);
            require('utils').dump(data);
        });
    },

    // 解释分页数据
    parsePages: function(key, val) {
        data[key] = [];
        if ('string' === typeof val.page.num) {
            val.page.num = IBBD.getSelectorInt(val.page.num);
        }
        casper.echo("需要抓取的页面数： " + val.page.num);
        IBBD.current_page = 1;
        IBBD.have_next_page = true;

        do {
            IBBD.parseOnePage(IBBD.current_page, key, val);
            IBBD.current_page++;
        } while(IBBD.current_page <= val.page.num);
    },

    // 解释一页的数据
    parseOnePage: function(current_page, key, val) {
        //casper.waitForSelector(val.selector, function() {
        casper.then(function() {
            IBBD.debug("当前抓取的页码是：" + current_page);
            IBBD.debug('页面显示当前的页码是：' + IBBD.evaluateSelector('span[class="current"]'));
            if (IBBD.have_next_page) {
                var one_page_data = null;
                if ('table' === val.type) {
                    one_page_data = IBBD.table(val);
                } else if ('list' === val.type) {
                    one_page_data = IBBD.list(val);
                }

                IBBD.debug(one_page_data);
                data[key].push(one_page_data);

                // 截图
                this.captureSelector('edy-'+current_page+'.png', '.company_center');
            }
        });
        
        casper.then(function() {
            // 点击页面
            if (casper.exists(val.page.next) && current_page < val.page.num) {
                var begin_time = Date.now();
                this.click(val.page.next);

                // test
//                if (1 === current_page) {
//                    this.click(val.page.next);
//                }
                IBBD.sleep(val.page.delay * 1000);
                IBBD.debug("点击下一页，耗时：" + (Date.now() - begin_time));
            } else {
                IBBD.have_next_page = false;
            }
        }); 
    },

    // 表格数据解释
    table: function(config) {
        IBBD.debug('抓取表格数据');
        return casper.evaluate(function(ibbd_config, ibbd_format) {
            var rows = document.querySelectorAll(ibbd_config.selector);
            var table_data = [];
            for (var i in rows) {
                if (false === /\d/.test(i)) {
                    continue;
                }
                if ('number' === typeof ibbd_config.first_row && i < ibbd_config.first_row) {
                    continue;
                }
                if ('number' === typeof ibbd_config.last_row && i >= ibbd_config.last_row) {
                    continue;
                }

                var row = rows[i];
                var one_data = {};
                for (var j in ibbd_config.cols) {
                    var col = ibbd_config.cols[j];
                    one_data[j] = row.children[col.col].innerText;
                    one_data[j] = ibbd_format(one_data[j], col);
                }

                table_data.push(one_data);
            }

            return table_data;
        }, config, IBBD.format);
    },

    // 列表数据解释
    list: function(config) {
        IBBD.debug('抓取列表数据');
        return casper.evaluate(function(ibbd_config, ibbd_format) {
            var IBBDParseData = function(ibbd_config, ibbd_format) {
                var rows = document.querySelectorAll(ibbd_config.selector);
                var list_data = [];

                // debug 
                //list_data.push(document.querySelector(ibbd_config.selector).innerHTML);

                for (var i in rows) {
                    if (false === /\d/.test(i)) {
                        continue;
                    }
                    if ('number' === typeof ibbd_config.first_row && i < ibbd_config.first_row) {
                        continue;
                    }
                    if ('number' === typeof ibbd_config.last_row && i >= ibbd_config.last_row) {
                        continue;
                    }

                    var row = rows[i];
                    var one_data = {};
                    for (var j in ibbd_config.cols) {
                        var col = ibbd_config.cols[j];
                        var col_dom = null;
                        if ('string' === typeof col.selector) {
                            col_dom = row.querySelector(col.selector);
                        } else if ('number' === typeof col.col) {
                            col_dom = row.children[col.col];
                        }

                        if ('string' === typeof col.attr) {
                            one_data[j] = col_dom.getAttribute(col.attr);
                        } else {
                            one_data[j] = col_dom.innerText;
                        }
                        one_data[j] = ibbd_format(one_data[j], col);
                    }

                    list_data.push(one_data);
                }

                return list_data;
            };  // end of IBBDParseData

            return IBBDParseData(ibbd_config, ibbd_format);
        }, config, IBBD.format);
    }
};

//************************* 以下是主体流程 *********************

var casper = require('casper').create(page_task.browser);

casper.start(page_task.url, function() {
    this.echo(this.status(true));
});

casper.then(function() {
    this.scrollToBottom();
    this.echo('scroll to bottom');
});

// 前置动作
if (page_task.pre_op.length > 0) {
    IBBD.pre_op(page_task.pre_op);
}

// 解释变量
for (var k in page_task.vars) {
    casper.echo("-------------------------" + k);
    var v = page_task.vars[k];
    if ('object' === typeof v.page) {
        IBBD.parsePages(k, v);
    } else {
        IBBD.parse(k, v);
    }
}

casper.run(function() {
    require('utils').dump(data.length);
    this.exit();
});
