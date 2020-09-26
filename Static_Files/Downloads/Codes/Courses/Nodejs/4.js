const http = require('http')

const server = http.createServer((req, res) => {

    if(req.url === '/') {
        res.write("Hello World")
        res.end()
    } else {
        res.write("This is not Hello World Page")
        res.end()
    }

});

server.listen(3000)


const express = require('express')
const app = express()

app.get('/', (req, res) => {
    res.send("Hello World")
})

app.get('/node', (req, res) => {
    res.send("This is not Hello World Page")
})

app.listen(3000, () => {
    console.log("Server is Running....")
})