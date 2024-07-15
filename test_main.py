import unittest
from calculator import add, multiply

class TestMain(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-2, 2), 0)
        self.assertEqual(add(0, 0), 0)
    
    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(0, 0), 0)
        self.assertEqual(multiply(-2, 3), -6)
        self.assertEqual(multiply(-2, -3), 6)
    
if __name__ == "__main__":
    unittest.main()
