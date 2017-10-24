import falcon


class ReportResource:

    def on_post(self, request, response):
        response.status = falcon.HTTP_204
