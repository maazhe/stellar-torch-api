#!/usr/bin/python3
# coding: utf8

from jinja2 import Environment, FileSystemLoader
from aiohttp import web
import config

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

def get_data_dict():
    return {
        'latlngs' : config.LATLNGS,
        'distanceCovered': 0
    }

def get_home(request):
    template = env.get_template('home.html')
    data = get_data_dict()
    page = template.render(data=data)
    return web.Response(text=page, content_type='text/html')