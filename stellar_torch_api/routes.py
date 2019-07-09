#!/usr/bin/python3
# coding: utf8

from aiohttp import web
import stellartorchserver

def setup_routes(app):
    app.router.add_get('/' , stellartorchserver.get_home)

    # other static
    app.router.add_static('/static/', path='./static/', name='static')
    app.router.add_static('/templates/', path='./templates/', name='templates')