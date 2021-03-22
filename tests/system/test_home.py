from tests.system.base_test import BaseTest
from unittest.mock import patch

class TestHome(BaseTest):

    def test_home(self):
        with self.app() as c:
            resp=c.get('/')
            self.assertEqual(resp.status_code,200)
            with patch('flask.render_template') as mocked_template:
                c.run_wsgi_app()
                mocked_template.assert_called()