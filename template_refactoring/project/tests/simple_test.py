from unittest import TestCase

class SimpleTest(TestCase):
    def test_add_one_and_two(self):
        self.assertEqual(3,1+2)
