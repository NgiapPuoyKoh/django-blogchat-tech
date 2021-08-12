from django.test import TestCase
from blog.forms import NewCommentForm


class NewCommentFormTest(TestCase):

    def test_comment_form_valid_data(self):
        form = NewCommentForm(data = {
            'name': 'Commentor Name',
            'email': 'comentor@email.com',
            'content': 'Comment on blog entered by commentor'
        })

        self.assertTrue(form.is_valid())

    def test_comment_form_no_data(self):
        form = NewCommentForm(data ={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 3)
