var fs = require('fs');
var casper = require('casper').create({
    verbose: true,
    logLevel: "debug"
});

var save_txt = JSON.stringify({ab:123});
casper.echo(save_txt);
require('utils').dump(fs);

fs.writeFile('/tmp/test.txt', save_txt, function (err) {
    console.log('Saved');
});

fs.readFile('/tmp/test.txt', 'utf8', function(err, data) {
    console.log(data);
});

casper.run();
