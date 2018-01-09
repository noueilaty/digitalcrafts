const express = require('express');
const app = express()
const mustacheExpress = require('mustach-express')
app.engine('mustache',mustacheExpress())

// mustache pages will be inside the views folder
app.set('views','/views')
app.set('view engine', 'mustache')

app.get('/dishes', function(req,res) {
  
})

app.get('/', function(req, res) {
  res.send('Hello world');
});

app.listen(3000, () => console.log('Example app listening on port 3000!'))
