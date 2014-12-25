var casper = require('casper').create();

casper.start('http://www.ibbd.net/', function() {
    this.echo(this.getTitle());
});

casper.run();
