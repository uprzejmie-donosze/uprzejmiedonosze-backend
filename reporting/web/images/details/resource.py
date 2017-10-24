import json


class DetailsImageResource:

    def on_post(self, request, response):
        response.body = json.dumps({
            'plate_id': 'WX 4324W',
            'brand': 'Jeep',
        })
