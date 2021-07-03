from django.test import TestCase

# Create your tests here.
class TestViews(TestCase):
    def test_fail_donate_page(self):
        """ TDD Fail Render Donate Page """
        response = self.client.get('/donate/')
        self.assertEqual(response.status_code, 302)


    # /donate/charge/100 will redirect to  /donate/success/100/
    # /donate/charge/ will redirect to /donate/success/5/
    # html page amount will be updated to donated amount
    # back to donation page link
    # def test_charge(self):
        """Test charge stripe """


    def test_donate_page(self):
        """ Test donate page renders donate.html """
        response = self.client.get('/donate/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'donate/donate.html')


    
    def test_successMsg(self):
        """Test donate success renders success.html with amount"""
        amount = 10
        response = self.client.get(f'/donate/success/{amount}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'donate/success.html')


    # def test_donate_link

    
