/**
 * 入口文件
 * Usages:
 * casperjs index.js cninfo
 */

(function() {
    var browser_config = {
        verbose: true,
        logLevel: "debug",

        // 浏览器size
        viewportSize: {width: 800, height:1200},

        userAgent: 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/39.0.2171.65 Chrome/39.0.2171.65 Safari/537.36',

        pageSettings: {
            loadImages:  false,        // The WebPage instance used by Casper will
            loadPlugins: false         // use these settings
        }
    };

    var casper = window.casper = require('casper').create(browser_config);
    var IBBD = require('libs/ibbd.js').create();

    // 加载配置
    var config_file = 'config/' + casper.cli.args[0] + '_config.js';
    var tasks = require(config_file).config;
    IBBD.debug('config');
    IBBD.debug(tasks);

    // 任务
    casper.start();
    IBBD.task.init();
    IBBD.task.add(tasks);
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

})();

