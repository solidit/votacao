# -*- encoding: utf-8 -*-

from piston.handler import BaseHandler
from piston.utils import rc, throttle

from django.core.cache import cache

def votar(candidato):
    votos = cache.get(candidato)
    if type(votos) == 'NoneType':
        votos = 1
    votos = votos + 1
    return cache.set(candidato,votos,timeout=0)

class VotarAHandler(BaseHandler):
    allowed_methods = ( "GET", )

    def read(self, request ):
        if request.method == "GET":
            return votar("A")
        else:
            return False

class VotarBHandler(BaseHandler):
    allowed_methods = ( "GET", )

    def read(self, request ):
        if request.method == "GET":
            return votar("B")
        else:
            return False

class ResultadoHandler(BaseHandler):
    allowed_methods = ( "GET", )

    def read(self, request):
        if request.method == "GET":
            return {"A": cache.get("A"), "B": cache.get("B")}
        else:
            return False