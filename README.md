# EX01 Developing a Simple Webserver
## Date:09/09/2025

## AIM:
To develop a simple webserver to serve html pages and display the Device Specifications of your Laptop.

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
```-
from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html>
    <head>
        <title>
            WEB DEVELOPEMENT
        </title>
    </head>
    <body bgcolor="blue">
        <h1 bgcolor="red" align="center">DEVICE SPECIFICATIONS (SACHIN J M)</h1>
        
    </body>
</html>

<html>
    <head>
        
    </head>
    <body>
        <table color="red" border="5" align="center" cellpadding="2" cellspacing="2">
            <tr bgcolor="cyan">
                <th>S.NO</th>
                <th>MODEL WITH COMPANY</th>
                <th>CAMERA SPECIFICATIONS</th>
            </tr>
            <tr bgcolor="green">
                <td>1</td>
                <td>VIVO Y19</td>
                <td>50mp</td>
            </tr>
            <tr bgcolor="red">
                <td>2</td>
                <td>REALME GT PRO</td>
                <td>50mp</td>
            </tr>
            <tr bgcolor="blue">
                <td>3</td>
                <td>INFINIX GT20 PRO</td>
                <td>108mp</td>
            </tr>
            <tr bgcolor="orange">
                <td>4</td>
                <td>ONEPLUS NORD CE5</td>
                <td>58mp</td>
            </tr>
            <tr bgcolor="white">
                <td>5</td>
                <td>I PHONE</td>
                <td>50mp</td>
            </tr>

        </table>
    </body>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()
```

## OUTPUT:
![alt text](<Screenshot 2025-09-16 144818.png>)
![alt text](<Screenshot 2025-09-16 144840.png>)


## RESULT:
The program for implementing simple webserver is executed successfully.
