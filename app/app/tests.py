"""
Sample tests
"""

from django.test import SimpleTestCase

from app import calc

class CalcTests(SimpleTestCase):
    """Test the calc module."""
    
    def test_add_numbers(self):
        """Test adding numbers together."""
        res = calc(5, 6)
        
        self.assert(res, 11)