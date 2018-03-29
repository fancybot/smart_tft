#About How To run the server
nohup node server.js > output.log &

#How to stop the server.js

ps aux |grep node server.js
kill -9 +[pid]


