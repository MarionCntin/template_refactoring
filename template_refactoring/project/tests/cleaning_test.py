from unittest import TestCase
from project.cleaning.cleaning import Cleaning
import pandas as pd

class TestCleaning(TestCase):

    def test_data_are_cleaned(self):
        self.assertEqual(3,1+2)
        
