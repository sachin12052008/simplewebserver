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