var fs = require('fs');

console.log(fs);

fs.writeFile('/tmp/hello', 'test');

fs.unlink('/tmp/hello', function (err) {
    if (err) throw err;
    console.log('successfully deleted /tmp/hello');
});
