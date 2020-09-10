from unittest import TestCase

from Problema7 import crecimiento


class Test(TestCase):
    def test_crecimiento(self):
        self.assertEqual(58,crecimiento())