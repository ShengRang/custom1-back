import tornado.web
import json
from tornado_cors import CorsMixin

class base_handler(CorsMixin, tornado.web.RequestHandler):
    # Value for the Access-Control-Allow-Origin header.
    # Default: None (no header).
    CORS_ORIGIN = '*'

    # Value for the Access-Control-Allow-Headers header.
    # Default: None (no header).
    CORS_HEADERS = 'Content-Type'

    # Value for the Access-Control-Allow-Methods header.
    # Default: Methods defined in handler class.
    # None means no header.
    CORS_METHODS = 'POST GET'

    # Value for the Access-Control-Max-Age header.
    # Default: 86400.
    # None means no header.
    CORS_MAX_AGE = 21600

    def get_current_user(self):
       return self.get_secure_cookie('user', 0)

    def get_json_argument(self, name):
        return json.loads(self.request.body.decode("utf-8") )[name]

class forbiden_handler(base_handler):
    def get(self):
        raise tornado.web.HTTPError(403)
    def post(self):
        raise tornado.web.HTTPError(403)

