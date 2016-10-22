from openalpr import Alpr

import json
import tornado.ioloop
import tornado.web

alpr = Alpr("eu", "/etc/openalpr/openalpr.conf", "/usr/share/openalpr/runtime_data")
alpr.set_top_n(20)



class MainHandler(tornado.web.RequestHandler):
    def get(self):
        html = """
                <html>
                <title>Openalpr Webservice</title>
                <script src="//ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js"></script> 
                <body>
                    <h2>Tesseract Web Service</h2>
                    <form name="mainForm" id="mainForm" action="" method="POST" enctype="multipart/form-data">
                        Target image url: <input type="text" id="image" name="image" size="80" />
                        <input id="submitBtn" type="submit" value="Submit" />
                    </form>
                    <div id="result"></div>
                </body>
                </html>
               """
        self.write(html)
    def post(self):

        if 'image' not in self.request.files:
            self.finish('Image parameter not provided')

        fileinfo = self.request.files['image'][0]
        jpeg_bytes = fileinfo['body']

        if len(jpeg_bytes) <= 0:
            return False

        results = alpr.recognize_array(jpeg_bytes)

        self.finish(json.dumps(results))



application = tornado.web.Application([
    (r"/alpr", MainHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()