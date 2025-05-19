# EX01 Developing a Simple Webserver
## Date: 19.05.25

## AIM:
To develop a simple webserver to serve html pages and display the list of protocols in TCP/IP Protocol Suite.

## DESIGN STEPS:
### Step 1: 
HTML content creation.

### Step 2:
Design of webserver workflow.

### Step 3:
Implementation using Python code.

### Step 4:
Import the necessary modules.

### Step 5:
Define a custom request handler.

### Step 6:
Start an HTTP server on a specific port.

### Step 7:
Run the Python script to serve web pages.

### Step 8:
Serve the HTML pages.

### Step 9:
Start the server script and check for errors.

### Step 10:
Open a browser and navigate to http://127.0.0.1:8000 (or the assigned port).

## PROGRAM:

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


## OUTPUT:
![alt text](<Screenshot 2025-05-19 102102.png>)

![alt text](<Screenshot 2025-05-19 102431.png>)

## RESULT:
The program for implementing simple webserver is executed successfully.
