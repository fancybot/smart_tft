
//express_demo.js 文件
var express = require('express');
var app = express();
 

app.use(express.static('public'));


app.get('/', function (req, res) {
   res.send('Hello World');
})
 
app.get('/page', function (req, res) {
   res.send('Hello World>>page');
})

app.get('/data', function (req, res) {
   res.send('Hello World>>data');
})

app.get('/log', function (req, res) {
   res.send('Hello World>>log');
})

app.get('/index.htm', function (req, res) {
   res.sendFile( __dirname + "/" + "index.htm" );
})
 
app.get('/process_get', function (req, res) {
 
   // 输出 JSON 格式
   var response = {
       "first_name":req.query.first_name,
       "last_name":req.query.last_name
   };
   console.log(response);
   res.end(JSON.stringify(response));
})

var server = app.listen(80, function () {
 
  var host = server.address().address
  var port = server.address().port
 
  console.log("应用实例，访问地址为 http://%s:%s", host, port)
  console.log('Server running at http://127.0.0.1:/80');
  console.log('Visit http://119.23.220.55');
 
})



