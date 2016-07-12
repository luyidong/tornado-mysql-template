#!/usr/bin/env python
#coding=utf-8
#__author__  = louis,
# __date__   = 2016-07-11 14:44,
#  __email__ = yidongsky@gmail.com,
#   __name__ = cmdb.py

import tornado.web



class index(tornado.web.RequestHandler):
    def get(self):
        #greeting = self.get_argument('greeting', 'Hello')
        #self.write(greeting + ', friendly user!')
        self.render("base/index.html")
