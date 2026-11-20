const http = require('http');

const PORT = process.env.PORT || 3000;

const server = http.createServer((req, res) => {
    res.statusCode = 200;
    res.setHeader('Content-Type', 'application/json');
    res.end(JSON.stringify({
        status: 'SUCCESS',
        message: 'DevOps Lab 1 Application Running',
        timestamp: new Date().toISOString()
    }));
});

server.listen(PORT, () => {
    console.log(`Server listening on port ${PORT}`);
});
