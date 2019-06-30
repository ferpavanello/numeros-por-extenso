from http.server import BaseHTTPRequestHandler, HTTPServer
from controle import controle


class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        url = self.path
        self._set_headers()
        self.wfile.write(
            bytes("<html><head><title>Teste</title></head>", "utf-8"))
        self.wfile.write(
            bytes(f"<body><p>{controle('55118')}</p>", "utf-8"))


def run(server_class=HTTPServer, handler_class=S, port=3000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print('Starting httpd...')
    httpd.serve_forever()


if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
