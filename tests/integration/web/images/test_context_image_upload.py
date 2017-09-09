import webtest

from reporting.main import main


class TestContextImageUploadEndpoint:

    def setup_method(self):
        self.container = main()

    def test_image_upload_returns_response(self) -> None:
        app = webtest.TestApp(self.container('web.wsgi.app'))
        response = app.post('http://localhost:8000/image')
        assert response.json == {
            'image_url': 'images/123.jpg',
            'image_thumb_url': 'images/123.jpg',
            'address': 'Żurawia 3/5, 00-503, Warszawa',
        }
