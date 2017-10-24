import webtest

from reporting.main import main


class TestDetailsImageUploadEndpoint:

    def setup_method(self):
        self.container = main()

    def test_image_upload_returns_response(self) -> None:
        app = webtest.TestApp(self.container('web.wsgi.app'))
        response = app.post('http://localhost:8000/image/details')
        assert response.json == {
            'plate_id': 'WX 4324W',
            'brand': 'Jeep',
        }
