from django.test import TestCase
from .forms import DepartmentForm

class DepartmentFormTest(TestCase):
    def test_valid_form(self):
        form_data = {'name': 'backend'}
        form = DepartmentForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_empty_form(self):
        form_data = {}
        form = DepartmentForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['name'], ['This field is required.'])

