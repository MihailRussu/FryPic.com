__author__ = 'rm'

import webapp2
from webapp2_extras import jinja2


class RequestHandler(webapp2.RequestHandler):
    @webapp2.cached_property
    def jinja2(self):
        return jinja2.get_jinja2(app=self.app)

    def render_response(self, _template, **context):
        rv = self.jinja2.render_template(_template, **context)
        self.response.write(rv)


class MainHandler(RequestHandler):
    def get(self):
        self.render_response('main.html')


