import os

import tornado.httpclient
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from pyrestful import rest

from health import health_v1_http

tornado.options.define('port', type=int, default=8000, help='server port number (default: 8000)')
tornado.options.define('debug', type=bool, default=True, help='run in debug mode with autoreload (default: False)')

root = os.path.dirname(__file__)

application = rest.RestService([
    health_v1_http.HealthResource
])


def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(tornado.options.options.port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()
