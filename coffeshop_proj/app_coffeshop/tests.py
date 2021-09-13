from django.test import TestCase
from app_coffeshop.models import Product


class ModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Product.objects.create(title='sperso')

    def test_title_label(self):
        product = Product.objects.get(title='sperso')
        field_label = product._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title')


# class YourTestClass(TestCase):
#     def setUp(self):
#         # Setup run before every test method.
#         pass

#     def tearDown(self):
#         # Clean up run after every test method.
#         pass

#     def test_something_that_will_pass(self):
#         self.assertFalse(False)

#     def test_something_that_will_fail(self):
#         self.assertTrue(False)
