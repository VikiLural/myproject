from wsgiref.simple_server import make_server

STATUS = '200 OK'
TYPE = 'text/HTML'

def app(environ, start_response):
    start_response(STATUS, [('Content-type', TYPE)])
    openfile = open(environ['PATH_INFO'], 'r')
    return openfile

class Middleware(object):
    def __init__(self, app):
        self.app = app
    def __call__(self, environ, start_response):
        for strk in self.app(environ, start_response):
            if strk.find('<body>') > 0: yield strk.encode() + "\t<div class='top'>Middleware TOP</div> \n".encode()
            elif strk.find('</body>') > 0: yield "\t<div class='bottom'>Middleware BOTTOM</div> \n".encode() + strk.encode()
            else: yield strk.encode()

server = make_server('127.0.0.1', 8000, Middleware(app))
server.serve_forever()