
//require('utils');

//console.log('%0$s,%0$s,%1$s'.format(23,32453));
//
//console.log("asd ".trim() + '|');
//console.log("    sff ".trim() + '|');

var optparse = require('optparse');

var switches = [
    ['-h', '--help', 'Shows help sections'],
    ['-h', '--help', 'Shows help sections']
];

var parser = new optparse.OptionParser(switches);

parser.banner = 'Usage: test.js [options]';

parser.on('help', function() {
    console.log(parser.toString());
});

parser.on('*', function(opt, value) {
    console.log('wild handler for ' + opt + ', value=' + value);
});

parser.parse(process.argv);
