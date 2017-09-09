import json


class ContextImageResource:

    def on_post(self, request, response):
        response.body = json.dumps({
            'image_url': 'images/123.jpg',
            'image_thumb_url': 'images/123.jpg',
            'address': 'Żurawia 3/5, 00-503, Warszawa'
        })
