def sum (a,b):
    return a + b

def sub (a,b):
    return a - b

def div (a,b):
    if b != 0:
        return a/b

def mult (a,b):
    return a * b

import unittest

class TestSum(unittest.TestCase):
    def test_sum_positive(self):
        self.assertEqual(sum(2,3),5)

    def test_sum_negative(self):
        self.assertEqual(sum(-5,-3), -8)

    def test_sum_zero(self):
        self.assertEqual(sum(0,0),0)
    
    def test_sum_postive_negative(self):
        self.assertEqual(sum(-4,2),-2)

class TestSub(unittest.TestCase):
    def test_sub_positive(self):
          self.assertEqual(sub(6,3),3)

    def test_sub_negative_float(self):
        self.assertEqual(sub(-6,-3), -3)

    def test_sub_zero(self):
        self.assertEqual(sub(0,0),0)
    
    def test_sub_positive_negative(self):
        self.assertEqual(sub(-6,2),-8)

class TestDiv(unittest.TestCase):
    def test_div_positive(self):
          self.assertEqual(div(8,2),4)

    def test_div_negative_float(self):
        self.assertEqual(div(-8,-5), 1.6)

    def test_div_zero1(self):
        self.assertEqual(div(2,0),None)

    def test_div_zero2(self):
        self.assertEqual(div(0,3),0)
    
    def test_div_positive_negative(self):
        self.assertEqual(div(-9,2),-4.5)

class TestMult(unittest.TestCase):
    def test_mult_positive(self):
          self.assertEqual(mult(12,2),24)

    def test_mult_negative(self):
        self.assertEqual(mult(-8,-2),16)

    def test_mult_zero(self):
        self.assertEqual(mult(0,0),0)
    
    def test_mult_positive_negative(self):
        self.assertEqual(mult(-7,2),-14)

if __name__ == '__main__':
    unittest.main()
