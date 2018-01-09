var app = require('express')();
var http = require('http').Server(app);
var io = require('socket.io')(http);

var participants = 0;

app.get('/', function(req, res){
  res.sendFile(__dirname + '/index.html');
});

io.on('connection', function(socket){
  console.log('a user conected');
  participants += 1;
  console.log('Participants: ', participants);
  socket.on('disconnect', function(){
    console.log('user disconnected');
    participants -= 1;
    console.log('Participants: ', participants);
  });
});

http.listen(3000, function(){
  console.log('listening on *:3000');
});

io.on('connection', function(socket){
  socket.on('chat message', function(msg){
    console.log('message: ' + msg);
  });
});

io.on('connection', function(socket){
  socket.on('chat message', function(msg){
    io.emit('chat message', msg);
  });
});
