from tornado.web import authenticated

from request_handlers.base_request_handler import BaseRequestHandler


class HomeHandler(BaseRequestHandler):

    @authenticated
    def get(self):
        #self.write({"you're logged in as": self.current_user})
        self.redirect('/static/index.html')