const http = require("http");

const Server = http.createServer(function(req, res) {
    res.write("Hello World, This is our fist app")
    res.end()
})

Server.listen(3000)

console.log("Server is Running...")