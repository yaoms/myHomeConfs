var net = require('net');

var server = net.createServer(function (socket) {
  socket.write('Echo server\n');
  //socket.pipe(socket);
  socket.on('data', function (data) {
	  if (data.trim() == 'quit') {
		socket.destroy();
	  } else {
	  	socket.write(data);
	  }
  });
});

server.listen(1337, '127.0.0.1');
