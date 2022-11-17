import unittest
import warnings

from apitable import Apitable
from . import TEST_TABLE, TEST_API_BASE, TEST_API_TOKEN


class TestGetFields(unittest.TestCase):

    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning)
        apitable = Apitable(TEST_API_TOKEN)
        apitable.set_api_base(TEST_API_BASE)
        self.dst = apitable.datasheet(TEST_TABLE)

    def test_fields_all(self):
        fields = self.dst.fields.all()
        self.assertIsInstance(fields, list)
        primary_field = fields[0]
        self.assertTrue(primary_field.isPrimary)
        self.assertEqual(primary_field.name, 'title')
        self.assertEqual(primary_field.type, 'SingleText')

    def test_field_get(self):
        primary_field = self.dst.fields.get('title')
        self.assertTrue(primary_field.isPrimary)
        self.assertEqual(primary_field.name, 'title')
        self.assertEqual(primary_field.type, 'SingleText')


if __name__ == '__main__':
    unittest.main()