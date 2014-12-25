
var page_task = {
    // 浏览器size
    viewportSize: {width: 800, height:2000},

    // 页面的URL
    url: 'http://chaoshi.detail.tmall.com/item.htm?&spm=a2156.1527398.1998335648.5.fxYbIl&acm=lb-tms-1527398-52798.1003.4.162758&scm=1003.4.lb-tms-1527398-52798.ITEM_39565447429_162758&userBucket=14&id=39565447429',

    // 前置动作
    pre_op: [
        {
            // 点击动作
            type: 'click',
            xpath: 'ul#J_TabBar li a[href="#J_DealRecord"]'
        }
    ],

    // 需要抓取的变量
    vars: {
        'title': {
            type:  'text',
            xpath: 'div.tb-detail-hd h1'
        },

        'price': {
            type:  'float',
            xpath: 'span.tm-price'
        },

        'count': {
            type:  'int',
            xpath: 'span.tm-count'
        },

        // 获取表格数据
        'deal_record': {
            type:  'table',
            xpath: 'div#J_showBuyerList table tbody tr',
            first_row: 1,
            cols: {
                username: {col: 0},
                type:     {col: 1},
                number:   {col: 2, type: 'int'},
                price:    {col: 3},
                time:     {col: 4, replace: ["\n", ' ']}
            }

            // 分页数据
            ,page: {
                num:  10,                 // 最多获取10页的数据
                next: 'div.page-bottom a:last-child',
                delay: 3
            }
        }

    }

};



// *********************************************

var IBBD = {
    sleep: function(sleep_time) {
        for (var start = Date.now(); Date.now() - start <= sleep_time; ); 
    },

    getInnerText: function(selector) {
        return document.querySelector(selector).innerText;
    },

    format: function(val, config) {
        val = val.trim();
        if ('string' === typeof config.type) {
            switch (config.type) {
                case 'int':
                    val = parseInt(val);
                break;
                case 'float':
                    val = parseFloat(val);
                break;
            }
        }

        if ('object' === typeof config.replace) {
            val = val.replace(config.replace[0], config.replace[1]);
        }

        return val;
    },

    evaluate: function(config) {
        return casper.evaluate(function(config) {
            var val = document.querySelector(config.xpath);
            return val.innerText;
        }, config);
    },

    pre_op: function(op_list) {
        // 前置动作
        for (var i in op_list) {
            var op = op_list[i];
            switch(op.type) {
                case 'click':
                    casper.waitForSelector(op.xpath, function() {
                    this.echo(op.xpath);
                    this.click(op.xpath);
                });
                break;
            }
        }
    },

    // 当前页码
    current_page: 1,

    // 解释变量
    parse: function(key, val) {
        casper.waitForSelector(val.xpath, function() {
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
        if ('table' === val.type) {
            data[key] = [];
            do {
                IBBD.parseOnePage(IBBD.current_page, key, val);
                IBBD.current_page++;
            } while(IBBD.current_page <= val.page.num);
        }
    },

    parseOnePage: function(current_page, key, val) {
        casper.waitForSelector(val.xpath, function() {
            if (current_page != this.evaluate(IBBD.getInnerText)) {
                return;
            }

            this.echo("========================" + key);
            if (casper.exists(val.page.next)) {
                var one_page_data = IBBD.table(val);
                data[key].push(one_page_data);
                require('utils').dump(data);
            }
        });

        casper.then(function() {
            if (current_page != this.evaluate(IBBD.getInnerText)) {
                return;
            }

            // 点击页面
            if (casper.exists(val.page.next)) {
                this.click(val.page.next);
                IBBD.sleep(val.page.delay * 1000);
            }
        }); 
    },

    // 表格数据解释
    table: function(config) {
        return casper.evaluate(function(config, format) {
            var rows = document.querySelectorAll(config.xpath);
            var data = [];
            for (var i in rows) {
                if (false === /\d/.test(i)) {
                    continue;
                }
                if ('number' === typeof config.first_row && i < config.first_row) {
                    continue;
                }
                if ('number' === typeof config.last_row && i >= config.last_row) {
                    continue;
                }

                //data.push(i);
                var row = rows[i];
                var one_data = {};
                for (var j in config.cols) {
                    var col = config.cols[j];
                    one_data[j] = row.children[col.col].innerText;
                    one_data[j] = format(one_data[j], col);
                }

                data.push(one_data);
            }

            return data;
        }, config, IBBD.format);
    }
};

var casper = require('casper').create({
    verbose: true,
    logLevel: "debug",
    viewportSize: page_task.viewportSize
});

casper.start(page_task.url, function() {
    this.echo(this.status(true));
});

casper.then(function() {
    this.scrollToBottom();
    this.echo('scroll to bottom');
});

// 前置动作
IBBD.pre_op(page_task.pre_op);

// 解释变量
var data = {};
for (var k in page_task.vars) {
    casper.echo("-------------------------" + k);
    var v = page_task.vars[k];
    if ('object' === typeof v.page) {
        IBBD.current_page = 1;
        IBBD.parsePages(k, v);
    } else {
        IBBD.parse(k, v);
    }
}

casper.run(function() {
    //require('utils').dump(data);
    require('utils').dump(data.length);
    this.exit();
});
