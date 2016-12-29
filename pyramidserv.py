from pyramid.response import Response
from pyramid.config import Configurator
from wsgiref.simple_server import make_server

def index(request):
    pRefAboutMe = '<p><a href="about/aboutme.html">Прямая ссылка</a></p>'
    aRefAboutMe = '<p><a href="http://127.0.0.1:8000/about/aboutme.html">абсолютная ссылка</a></p>'
    IndexPage = pRefAboutMe + aRefAboutMe
    return Response(IndexPage)
def aboutme(request):
    pRefIndex = '<p><a href="../">Прямая ссылка</a></p>'
    aRefIndex = '<p><a href="http://127.0.0.1:8000/">Абсолютная ссылка</a></p>'
    AboutMePage = pRefIndex + aRefIndex
    return Response(AboutMePage)

if __name__ == '__main__':
    configur = Configurator()
    configur.add_view(index, route_name='index')
    configur.add_route("index",'/')
    configur.add_view(aboutme, route_name='aboutme')
    configur.add_route('aboutme', 'about/aboutme.html')
server = make_server('127.0.0.1', 8000, configur.make_wsgi_app())
server.serve_forever()