from jinja2 import Environment, FileSystemLoader
from wsgiref.simple_server import make_server

fstemplates = FileSystemLoader('templates')
STATUS = '200 OK'
TYPE = 'text/HTML'

def app(environ, start_response):
    envir = Environment(loader=fstemplates)
    start_response(STATUS, [('Content-Type', TYPE)])
    pathinfo = environ['PATH_INFO']
    result = envir.get_template(pathinfo).render(link=pathinfo)
    return [result.encode('utf-8')]

server = make_server('127.0.0.1', 8000, app)
server.serve_forever()