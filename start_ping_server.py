import http.server
import socketserver
import socket

class PrintIpHandler(http.server.SimpleHTTPRequestHandler):
    def handle_one_request(self):
        print(f'Raspberry Pi IP address: {self.client_address[0]}')
        return http.server.SimpleHTTPRequestHandler.handle_one_request(self)

port = 8000
with socketserver.TCPServer(("", port), PrintIpHandler) as httpd:
    print(f"Current IP is: {socket.gethostbyname_ex(socket.gethostname())[-1][0]}")
    print("Serving at port", port)
    print("This server is used for the raspberry pi to send its IP address so that we can connect with SSH")
    httpd.serve_forever()