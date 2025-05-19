from http.server import BaseHTTPRequestHandler, HTTPServer

# HTML content with corrected formatting
content = """
<!DOCTYPE html>
<html>
<head>
    <title>PC CONFIGURATION</title>
</head>
<body>
    <center>
        <h2>PC CONFIGURATION</h2>
        <table border="2" bgcolor="aqua" cellpadding="10" cellspacing="5">
            <tr>
                <th>CONFIGURATION</th>
                <th>DESCRIPTION</th>
            </tr>
            <tr>
                <td>Device Name</td>
                <td>Jaseer-Desktop</td>
            </tr>
            <tr>
                <td>Processor</td>
                <td>13th Gen Intel(R) Core(TM) i5-1335U   1.30 GHz</td>
            </tr>
            <tr>
                <td>Version</td>
                <td>24H2</td>
            </tr>
            <tr>
                <td>Memory</td>
                <td>512 GB</td>
            </tr>
            <tr>
                <td>Graphics</td>
                <td>NVIDIA</td>
            </tr>
        </table>
    </center>
</body>
</html>
"""

# HTTP request handler class
class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("GET request received...")
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(content.encode())

# Start the server
if __name__ == "__main__":
    print("This is my webserver")
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, MyServer)
    httpd.serve_forever()
