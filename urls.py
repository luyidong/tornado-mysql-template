#!/usr/bin/env python
#coding=utf-8
#__author__  = louis,
# __date__   = 2016-04-20 01:13,
#  __email__ = yidongsky@gmail.com,
#   __name__ = urls.py

import tornado.web as web

from handlers.index import index

handlers = [
   #路由列表
   (r"/",index),


   (r"/static/(.*)", web.StaticFileHandler,{"path":"/Users/louis/PycharmProjects/fable/static"}),
]
#uiModules = {'Hello': HelloModule}


