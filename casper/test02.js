var links = [];
var casper = require('casper').create({
    verbose: true,
    logLevel: "debug"
});

function getLinks() {
    var links = document.querySelectorAll('.result h3 a');
    return Array.prototype.map.call(links, function(e) {
        return e.getAttribute('href');
    });
}

casper.start('http://www.baidu.com/', function() {
    this.echo(this.status(true));

    // search from baidu form
    //this.fill('form#form', { wd: 'ibbd' }, true);
    this.fill('form#form', { wd: '数据雷达' }, false);

    this.evaluate(function(){
        document.querySelector('form#form').submit();
    });
});

casper.then(function() {
    // aggregate results for the 'casperjs' search
    links = this.evaluate(getLinks);
    // search from baidu form
    //this.fill('form#form', { wd: 'php' }, true);
    this.fill('form#form', { wd: '迪奥科技' }, false);

    this.evaluate(function(){
        document.querySelector('form#form').submit();
    });
});

casper.then(function() {
    // aggregate results for the 'phantomjs' search
    links = links.concat(this.evaluate(getLinks));
});

casper.run(function() {
    // echo results in some pretty fashion
    this.echo(links.length + ' links found:');
    this.echo(' - ' + links.join('\n - ')).exit();
});
