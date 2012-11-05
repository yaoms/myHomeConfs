
require('utils');

var net = require('net');

var links = [];

var server = net.createServer(function (socket) {
    var addr = socket.remoteAddress + ':' + socket.remotePort;
    console.log('socket %j connected.', addr);
    for (var i in links) {
        if (/\d+/.test(i)) {
            links[i].socket.write('socket ' + addr + ' joined.\n');
        }
    }
    links.push({'socket':socket,'addr':addr});
    socket.write('Echo server\n');

    socket.on('data', function (data) {
        for (var i in links) {
            if (/\d+/.test(i)) {
                links[i].socket.write(links[i].addr + ': ' + data);
            }
        }
    });
    socket.on('end', function () {
        console.log('socket %j disconnected.', addr);
        for (var i in links) {
            if (/\d+/.test(i)) {
                if (links[i].socket == socket) {
                    links.remove(links[i]);
                } else {
                    links[i].socket.write('socket ' + links[i].addr + ' disconnected.');
                }
            }
        }
    });
});

server.on('listening', function() {
    console.log('listening on %j', server.address());
});

server.listen(1337, '127.0.0.1');
