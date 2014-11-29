import bucket
import unittest


class BucketTestCase(unittest.TestCase):
    def setUp(self):
        self.app = bucket.app.test_client()

    def test_set(self):
        response = self.app.post('/set/foobar', data={'foobar': 'wangskata'})
        assert response.status_code == 200
        assert response.data == 'OK'

    def test_get(self):
        response = self.app.get('/get/foobar')
        assert response.status_code == 200
        assert response.data == 'wangskata'


if __name__ == '__main__':
    unittest.main()
