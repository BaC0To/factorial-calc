import unittest
from factorial import factorial_calc


class TestFactorial(unittest.TestCase):


        def test_factorial_of_zero(self):
                #Test factorial function with test_number = 0
                test_number = 0
                expected_result = 1
                self.assertEqual(factorial_calc(test_number), expected_result)

        def test_factorial_of_one(self):
                #Test factorial function with test_number = 1
                test_number = 1
                expected_result = 1
                self.assertEqual(factorial_calc(test_number), expected_result)

        def test_factorial_of_positive_values(self):
                #Test factorial function with numbers > 0
                test_number = 5
                expected_result = 120
                self.assertEqual(factorial_calc(test_number), expected_result)

        def test_factorial_of_negative_values(self):
                #Test factorial function with numbers < 0
                test_number = -3
                self.assertRaises(ValueError, factorial_calc, test_number)

        def test_factorial_of_wrong_type(self):
                #Test factorial function with numbers that are not of type int
                test_number1 = (3+5j)
                self.assertRaises(TypeError, factorial_calc, test_number1)
                test_number2 = True
                self.assertRaises(TypeError, factorial_calc, test_number2)
                test_number3 = "five"
                self.assertRaises(TypeError, factorial_calc, test_number3)
        

if __name__ == '__main__':
    unittest.main()
    