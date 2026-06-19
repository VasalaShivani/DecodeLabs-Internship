import unittest
import string
import math
from generator import generate_secure_password, calculate_entropy, get_security_strength

class TestPasswordGenerator(unittest.TestCase):

    def test_calculate_entropy(self):
        """Verify the Shannon Information Entropy calculations are mathematically correct."""
        # Standard case: length 16, alphanumeric pool (62)
        expected_entropy = 16 * math.log2(62)
        self.assertAlmostEqual(calculate_entropy(16, 62), expected_entropy)
        
        # Test boundary cases (zero or negative sizes)
        self.assertEqual(calculate_entropy(0, 62), 0.0)
        self.assertEqual(calculate_entropy(16, 0), 0.0)
        self.assertEqual(calculate_entropy(-5, 62), 0.0)

    def test_get_security_strength(self):
        """Ensure security categorization thresholds function correctly."""
        self.assertIn("Very Weak", get_security_strength(30.0))
        self.assertIn("Weak", get_security_strength(50.0))
        self.assertIn("Moderate", get_security_strength(70.0))
        self.assertIn("Strong", get_security_strength(100.0))
        self.assertIn("Very Strong", get_security_strength(140.0))

    def test_generate_password_length(self):
        """Confirm that the generated password matches requested length exactly."""
        lengths = [10, 15, 32, 64]
        for length in lengths:
            password, _ = generate_secure_password(length)
            self.assertEqual(len(password), length)

    def test_generate_password_invalid_args(self):
        """Verify invalid arguments raise appropriate exceptions."""
        # Zero or negative length
        with self.assertRaises(ValueError):
            generate_secure_password(0)
        with self.assertRaises(ValueError):
            generate_secure_password(-10)
            
        # Empty pool selection
        with self.assertRaises(ValueError):
            generate_secure_password(10, use_letters=False, use_digits=False, use_punctuation=False)
            
        # Requested length too short for guaranteed pool representation
        with self.assertRaises(ValueError):
            generate_secure_password(2, use_letters=True, use_digits=True, use_punctuation=True)

    def test_character_pool_guarantee(self):
        """Confirm that at least one character from each selected class is present."""
        # Generate several passwords to account for stochastic selection and verify guarantee
        for _ in range(50):
            password, _ = generate_secure_password(15, use_letters=True, use_digits=True, use_punctuation=True)
            
            has_letter = any(c in string.ascii_letters for c in password)
            has_digit = any(c in string.digits for c in password)
            has_symbol = any(c in string.punctuation for c in password)
            
            self.assertTrue(has_letter, "Password failed to include a letter.")
            self.assertTrue(has_digit, "Password failed to include a digit.")
            self.assertTrue(has_symbol, "Password failed to include a symbol.")

    def test_exclusive_pool_generation(self):
        """Verify that password contains ONLY the selected character classes."""
        # Digits only
        password, pool_size = generate_secure_password(10, use_letters=False, use_digits=True, use_punctuation=False)
        self.assertEqual(pool_size, len(string.digits))
        for char in password:
            self.assertIn(char, string.digits)
            self.assertNotIn(char, string.ascii_letters)
            self.assertNotIn(char, string.punctuation)

    def test_performance_efficiency(self):
        """Verify generation runs quickly and handles large inputs (O(N) performance check)."""
        import time
        start_time = time.perf_counter()
        
        # Generate a large password
        password, _ = generate_secure_password(10000)
        
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        
        self.assertEqual(len(password), 10000)
        # Should execute in less than 0.1 seconds under linear time join structure
        self.assertLess(execution_time, 0.1, f"Execution took too long: {execution_time:.4f}s")

if __name__ == "__main__":
    unittest.main()
