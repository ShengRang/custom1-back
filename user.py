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
        password = self.get_json_argument('password')
        print('%s, %s' % (name, password))
        user = User.objects.get(name=name, password=password)
        if user:
            self.set_secure_cookie('user_id', str(user.id))
            self.write(empty)
        else:
            #raise tornado.web.HTTPError(403)
            self.write('{"error": error}')

class user_info_handler(base_handler):
    def get(self):
        user_id = self.get_secure_cookie('user_id').decode()
        user = User.get_by_id(user_id)
        if not user:
            self.write('{"error": error}')
            self.finish()
        content = {
                'name' : user.name,
                'position' : user.position,
                'priority' : user.priority,
                }
        resp = json.dumps(content)
        self.write(resp)

class user_add(base_handler):
    def post(self):
        user = User(name = self.get_json_argument('name'),
                passwd = self.get_json_argument('password'),
                priority = self.get_json_argument('priority')
                )
        user.save()
        self.write(empty)
