#!/usr/bin/env python
# encoding: utf-8
import json
import tornado.web
from base import base_handler
from models import *
empty = ''

class user_ip_handler(base_handler):

    def get(self):
        """TODO: Docstring for get.

        :arg1: TODO
        :returns: TODO
        """
        content = {
                "ip" : self.request.remote_ip
                }
        resp = json.dumps(content)
        self.write(resp)

    def post(self):
        self.write('hello, world')

class login_handler(base_handler):
    def post(self):
        name = self.get_json_argument('name')
        passwd = self.get_json_argument('passwd')
        if name == passwd:
            self.set_secure_cookie('user', str(1))
            self.write(empty)
        else:
            raise tornado.web.HTTPError(403)

class user_info_handler(base_handler):
    def get(self):
        content = {
                'name' : 'admin',
                'position' : 'CEO',
                'priority' : 1,
                }
        resp = json.dumps(content)
        self.write(resp)

class user_add(base_handler):
    def post(self):
        user = User(name = self.get_json_argument('name'),
                passwd = self.get_json_argument('passwd'),
                priority = self.get_json_argument('priority')
                )
        user.save()
        self.write(empty)
