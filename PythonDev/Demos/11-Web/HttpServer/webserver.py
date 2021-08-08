import string, time
from os import curdir, sep
from http.server import BaseHTTPRequestHandler, HTTPServer
import mimetypes

class MyHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        
        try:
            mimeType = mimetypes.guess_type(self.path)[0]
            print(mimeType)
            
            if self.path.endswith(".zzz"):   # Our made-up dynamic content.
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                result = "You requested {0} on day {1} in {2}" \
                           .format(self.path,
                                   time.localtime()[7],
                                   time.localtime()[0])
                self.wfile.write(result.encode('utf-8'))

            else:
                f = open(curdir + sep + self.path)
                self.send_response(200)
                self.send_header('Content-type', mimeType)
                self.end_headers()
                    
                self.wfile.write(f.read().encode('utf-8'))
                f.close()
            
        except IOError:
            self.send_error(404,'File Not Found: %s' % self.path)
     
def main():
    try:
        server = HTTPServer(('', 8001), MyHandler)
        print('Started HTTP server...')
        server.serve_forever()
    except KeyboardInterrupt:
        print('Ctrl+C received, shutting down server')
        server.socket.close()

if __name__ == '__main__':
    main()

