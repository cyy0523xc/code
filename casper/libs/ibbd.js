var require = patchRequire(require);

var IBBD = {
    // 结果数据保存
    data: [],

    getData: function() {
        return IBBD.data;
    },

    getOneData: function(key) {
        return IBBD.data[key];
    },

    debug: function(msg) {
        require('utils').dump(msg);
    },

    // @param int sleep_time 单位：毫秒
    sleep: function(sleep_time) {
        var end = Date.now() + sleep_time;
        for (; Date.now() < end;) {}
    },

    // 执行某个动作，使其最少消耗一定的时间。单位：毫秒
    // @param int delay_time 需要延迟的时间（动作消耗的时间也计算在内）
    delay: function(do_func, delay_time) {
        var end = Date.now() + delay_time;
        do_func();
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

        // 字符串替换
        if ('object' === typeof config.replace) {
            val = val.replace(config.replace[0], config.replace[1]);
        }

        // 取子字符串
        if ('object' === typeof config.substr) {
            if (1 === config.substr.length) {
                val = val.substr(config.substr[0]).trim();
            } else if (2 === config.substr.length) {
                var tmp = config.substr[1];
                if (tmp < 0) {
                    tmp = val.length + tmp - config.substr[0];
                }
                val = val.substr(config.substr[0], tmp).trim();
            }
        }

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

    preOperate: function(op_list) {
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


    // 解释变量(没有分页的数据)
    parse: function(key, val) {
        casper.waitForSelector(val.selector, function() {
            switch (val.type) {
                case 'table':
                    IBBD.data[key] = IBBD.table(val);
                    break;

                case 'list':
                    IBBD.data[key] = IBBD.list(val);
                    break;

                default:
                    IBBD.data[key] = IBBD.evaluate(val);
                    IBBD.data[key] = IBBD.format(IBBD.data[key], val);
                    break;
            }
            this.echo("========================" + key);
            IBBD.debug(IBBD.data);
        });
    },

    // 解释分页数据
    processPages: function(key, val) {
        IBBD.data[key] = [];
        if ('string' === typeof val.page.num) {
            val.page.num = IBBD.getSelectorInt(val.page.num);
        }
        casper.echo("需要抓取的页面数： " + val.page.num);

        // 解释数据
        current_page = 1;
        casper.waitForSelector(val.selector, function() {
            IBBD.processOnePage(current_page, key, val);
        });
    },

    // 解释一页的数据
    processOnePage: function(current_page, key, val) {
        IBBD.debug("当前抓取的页码是：" + current_page);
        IBBD.debug('页面显示当前的页码是：' + IBBD.evaluateSelector(val.page.current));

        var one_page_data = null;
        if ('table' === val.type) {
            one_page_data = IBBD.table(val);
        } else if ('list' === val.type) {
            one_page_data = IBBD.list(val);
        }
        IBBD.data[key].push(one_page_data);
        //IBBD.data[key] = 'test';

        IBBD.debug(one_page_data[0]);
        IBBD.debug("元素的个数：" + one_page_data.length + "    data length = " + IBBD.data.length + '===' + IBBD.data[key].length);
        //IBBD.debug(IBBD.data[key]);
        //casper.captureSelector('edy-'+current_page+'.png', '.company_center');

        // 判断是否应该结束
        if (current_page >= val.page.num || !casper.exists(val.page.next)) {
            IBBD.debug('分页结束');
            return;
        }

        current_page++;
        IBBD.debug('开始进入下一页');
        casper.thenClick(val.page.next).then(function() {
            var begin_time = Date.now();
            IBBD.sleep(val.page.delay * 1000);
            IBBD.debug("点击下一页，耗时：" + (Date.now() - begin_time));
            casper.waitForSelector(val.selector, function() {
                IBBD.processOnePage(current_page, key, val);
            });
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

exports.create = function(options) {
    return IBBD;
};

