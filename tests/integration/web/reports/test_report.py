import webtest

from reporting.main import main


class TestDetailsImageUploadEndpoint:

    def setup_method(self) -> None:
        self.container = main()

    def test_image_upload_returns_response(self) -> None:
        app = webtest.TestApp(self.container('web.wsgi.app'))
        response = app.post_json(
            'http://localhost:8000/report',
            params={
                'street': '',
                'city': '',
                'voivodeship': '',
                'brand': '',
                'plate_id': '',
                'incident_type': '',
            })
        assert response.status_code == 204
