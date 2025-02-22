import unittest
from app import app
from test_data import test_array


class APITestApp(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_1_process_receipts(self):
        for receipt in test_array:
            response = self.client.post('/receipts/process', json=receipt)
            self.assertEqual(response.status_code, 200)

    def test_2_calculate_reward(self):
        from app import receipt_data
        for receipt in receipt_data.keys():
            response = self.client.get('/receipts/{}/points'.format(receipt))
            self.assertEqual(response.status_code, 200)
            self.assertEqual(receipt_data[receipt]['points'], response.get_json()['points'])


if __name__ == '__main__':
    unittest.main()
