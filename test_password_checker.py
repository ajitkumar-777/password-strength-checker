
import unittest
from password_checker import check_password_strength


class TestPasswordChecker(unittest.TestCase):

    def test_weak_password(self):
        strength, _ = check_password_strength("abc")
        self.assertEqual(strength, "Weak")

    def test_moderate_password(self):
        strength, _ = check_password_strength("Password1")
        self.assertEqual(strength, "Moderate")

    def test_strong_password(self):
        strength, _ = check_password_strength("Password1!")
        self.assertEqual(strength, "Strong")

    def test_suggestions_are_returned(self):
        _, suggestions = check_password_strength("abc")
        self.assertGreater(len(suggestions), 0)


if __name__ == "__main__":
    unittest.main()
