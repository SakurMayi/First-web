import http.server
import socketserver
import socket

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip

PORT = 3000

handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), handler) as httpd:
    print(f"服务器运行在 http://localhost:{PORT}")
    print(f"在手机上访问 http://{get_ip()}:{PORT}")
    httpd.serve_forever()