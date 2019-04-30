import sys
import BaseHTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler


HandlerClass = SimpleHTTPRequestHandler
ServerClass  = BaseHTTPServer.HTTPServer
protocol     = "HTTP/1.0"
mime_types = {'.jsonp': 'application/x-javascript'}

if sys.argv[1:]:
    port = int(sys.argv[1])
else:
    port = 8000
server_address = ('', port)
# use this line to only serve on localhost
# server_address = ('127.0.0.1', port)

HandlerClass.protocol_version = protocol
HandlerClass.extensions_map.update(mime_types)
httpd = ServerClass(server_address, HandlerClass)

sa = httpd.socket.getsockname()
print "Serving HTTP on", sa[0], "port", sa[1], "..."
httpd.serve_forever()

