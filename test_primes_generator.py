import unittest

from primes_generator import generate_primes

class TestPrimesGenerator(unittest.TestCase):
    def test_valid_prime(self):
        known_composites = [4, 6, 8, 10, 12]
        result = generate_primes(20)
        for num in result:
            self.assertNotIn(num, known_composites)

    def test_range(self):
        n = 30
        result = generate_primes(n)
        self.assertLessEqual(max(result), n)

    def test_lowest_prime(self):
        n = 30
        result = generate_primes(n)
        self.assertLessEqual(min(result), 2)

if __name__ == '__main__':
    unittest.main()
