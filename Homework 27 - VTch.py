import unittest

# ფუნქცია ამოწმებს მარტივია თუ არა რიცხვი. (მარტივია თუ მხოლოდ 1_ზე და საკუთარ თავზე იყოფა)
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

# გატესტე ფუნქცია'unittest'_ის დახმარებით.


class TestPrimeNumbers(unittest.TestCase):
    def test_is_primel(self):
        self.assertTrue(is_prime(5))
        self.assertFalse(is_prime(4))
