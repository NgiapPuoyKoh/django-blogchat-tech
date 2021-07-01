from django.test import TestCase

# Create your tests here.
class TestViews(TestCase):
    def test_fail_donate_page(self):
        """ Test donate page renders when user click on donate button  """
        response = self.client.get('/donate/')
        self.assertEqual(response.status_code, 302)

    def test_donate_page(self):
        """ Test donate page renders when user click on donate button  """
        response = self.client.get('/donate/')
        self.assertEqual(response.status_code, 200)
