import tornado.web
import tornado.ioloop


class MyHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('Hello, tornado')


def make_appication():
    return tornado.web.Application([
            (r'/', MyHandler),
        ])


if __name__ == '__main__':
    app = make_appication()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
