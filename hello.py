from http.server import HTTPServer, BaseHTTPRequestHandler

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write('Hello world'.encode())
def main():
    PORT=8082
    server = HTTPServer(('', PORT), Handler)
    server.serve_forever()

if __name__=='__main__':
    main()
