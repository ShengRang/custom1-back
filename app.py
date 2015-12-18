#!/usr/bin/env python3
# encoding: utf-8

import os
import re
from tornado.options import define, options
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.autoreload
from user import *
from account import *
from base import forbiden_handler
from mongoengine import connect

define("port", default=8888, help="run on the given port", type=int)
define("debug",default=True,help="Debug Mode",type=bool)
connect('test')
# define("mongo_host", default="127.0.0.1:3306", help="database host")
# define("mongo_database", default="quora", help="database name")

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
                (r'/u/info', user_info_handler),
                (r'/u/login', login_handler),
                (r'/forbiden', forbiden_handler),
                (r'/u/ip', user_ip_handler),
                (r'/c/tree', account_tree_handler),
                (r'/c/add', account_add_handler),
                (r'/c/(\d+)', account_handler),
                (r'/c/test', account_test_handler),
                (r'/c/meta/(\d+)', account_meta_handler),
                ]
        settings = dict(
            # template_path = os.path.join(os.path.dirname(__file__), "templates"),
            # static_path=os.path.join(os.path.dirname(__file__), "static"),
            debug = options.debug,
            # xsrf_cookies = True,
            cookie_secret = "81o0TzKaPpGtYdkL5gEmGepeuuYi7EPnp2XdTP1o&Vo=",
            login_url = "/forbiden",
            session_secret = '08091287&^(01',
            # session_dir=os.path.join(os.path.dirname(__file__), "tmp/session"),
        )
        tornado.web.Application.__init__(self, handlers, **settings)

if __name__ == '__main__':
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    instance = tornado.ioloop.IOLoop.instance()
    tornado.autoreload.start(instance)
    instance.start()

