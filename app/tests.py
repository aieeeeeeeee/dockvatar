import unittest
import dockvatar

class TestCase(unittest.TestCase):

    def setUp(self):
        dockvatar.app.config["TESTING"] = True
        self.app = dockvatar.app.test_client()

    def test_get_mainpage(self):
        page = self.app.post("/", data=dict(name="Aieeeeeeeee Docker"))
        assert page.status_code == 200
        assert 'Hello' in str(page.data)
        assert 'Aieeeeeeeee Docker' in str(page.data)

    def test_html_escaping(self):
        page = self.app.post("/", data=dict(name='"><b>TEST</b><!--'))
        assert '<b>' not in str(page.data)

if __name__ == '__main__':
    unittest.main()
