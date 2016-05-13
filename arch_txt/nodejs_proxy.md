# nodejs proxy

在javascript 中有一个跨域的问题，我在本地有一个网页想调用远程的API，所以在本地起一个代理服务器就可以解决这个问题。

下面的代码，/v1 开头的URL走 proxy，其他URL会 查找本地文件(static server)

```javascript
var http = require('http');
var url = require("url");
var path = require("path");
var fs = require("fs");

var proxy;
proxy = http.createServer(function (request, response) {

    var uri = url.parse(request.url).pathname;

    console.log(uri);

    if (uri.startsWith('/v1')) {

        var options = {
            host: '192.168.0.1', // 这里是代理服务器
            port: 8000, // 这里是代理服务器端口
            path: request.url,
            method: request.method,
            headers: request.headers
            // headers: {
            //     'Authorization': request.headers['authorization'],
            //     'X-Meta-Params': request.headers['x-meta-params']
            // }
        };

        console.log(request.headers);

        var req = http.request(options, function (res) {
            res.pipe(response); // 这个pipe很喜欢
        }).end();

    } else {

        var filename = path.join(process.cwd(), uri);
        var contentTypesByExtension = {
            '.html': "text/html",
            '.css': "text/css",
            '.js': "text/javascript"
        };

        fs.exists(filename, function (exists) {
            if (!exists) {
                response.writeHead(404, {"Content-Type": "text/plain"});
                response.write("404 Not Found\n");
                response.end();
                return;
            }

            if (fs.statSync(filename).isDirectory()) {
                filename += 'index.html';
            }

            fs.readFile(filename, "binary", function (err, file) {
                if (err) {
                    response.writeHead(500, {"Content-Type": "text/plain"});
                    response.write(err + "\n");
                    response.end();
                    return;
                }

                var headers = {};
                var contentType = contentTypesByExtension[path.extname(filename)];
                if (contentType) headers["Content-Type"] = contentType;
                response.writeHead(200, headers);
                response.write(file, "binary");
                response.end();
            });
        });

    }


}).listen(8080);


```

