import unittest
from index import compute_age

class TestCompute_age (unittest.TestCase):
    def test_compute_age (self):
        self.assertEqual(compute_age(2009), 'Minor')
        self.assertEqual(compute_age(1998), 'Youth')
        self.assertEqual(compute_age(1981), 'Elder')
        
if __name__ == '__main__':
    unittest.main()