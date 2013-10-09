# -*- encoding: utf-8 -*-

from django.conf.urls import patterns, url
from piston.resource import Resource

from ws.handlers.votacao import VotarAHandler, VotarBHandler
from ws.handlers.votacao import ResultadoHandler

VotarAResource = Resource(handler=VotarAHandler)
VotarBResource = Resource(handler=VotarBHandler)
ResultadoResource = Resource(handler=ResultadoHandler)

urlpatterns = patterns('',
    url(r'^votar/a/$', VotarAResource, { 'emitter_format': 'json' }),
    url(r'^votar/b/$', VotarBResource, { 'emitter_format': 'json' }),
    url(r'^resultado/$', ResultadoResource, { 'emitter_format': 'json' }, name='resultado_list'),
)