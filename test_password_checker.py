
import unittest
from password_checker import check_password_strength


class TestPasswordChecker(unittest.TestCase):
    
    def test_empty_password(self):
        strength, suggestions = check_password_strength("")
        self.assertEqual(strength, "Invalid")
        self.assertIn("Password cannot be empty.", suggestions)

    def test_whitespace_password(self):
        strength, _ = check_password_strength("   ")
        self.assertEqual(strength, "Invalid")


    def test_weak_password(self):
        strength, _ = check_password_strength("gnu")
        self.assertEqual(strength, "Weak")

    def test_moderate_password(self):
        strength, _ = check_password_strength("Python3")
        self.assertEqual(strength, "Moderate")

    def test_strong_password(self):
        strength, _ = check_password_strength("Python3!")
        self.assertEqual(strength, "Strong")

    def test_suggestions_are_returned(self):
        _, suggestions = check_password_strength("abc")
        self.assertGreater(len(suggestions), 0)
    
    def test_common_weak_password(self):
        strength, _ = check_password_strength("password")
        self.assertEqual(strength, "Weak")


if __name__ == "__main__":
    unittest.main()
