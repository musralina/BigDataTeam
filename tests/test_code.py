import unittest
from src.bigdatateam.code import is_prime, primes, checksum, pipeline


class PrimeFunctionsTestCase(unittest.TestCase):
    def test_is_prime(self):
        self.assertTrue(is_prime(2))
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(6))
        self.assertFalse(is_prime(8))
        self.assertFalse(is_prime(9))
        self.assertFalse(is_prime(-1))
        self.assertFalse(is_prime(0))

    def test_primes(self):
        primes_list = primes(5)
        self.assertEqual(len(primes_list), 5)
        self.assertTrue(all(is_prime(num) for num in primes_list))
        empty_list = primes(0)
        self.assertEqual(empty_list, [])

    def test_checksum(self):
        numbers = [1, 2, 3, 4]
        result = checksum(numbers)
        self.assertIsInstance(result, int)
        self.assertGreaterEqual(result, 0)
        self.assertLessEqual(result, 99999999)

    def test_pipeline(self):
        result = pipeline()
        self.assertIsInstance(result, int)
        self.assertGreaterEqual(result, 0)


if __name__ == "__main__":
    unittest.main()
