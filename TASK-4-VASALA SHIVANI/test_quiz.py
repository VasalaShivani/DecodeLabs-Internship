import unittest
from quiz import sanitize_input, evaluate_answer

class TestGeneralKnowledgeQuiz(unittest.TestCase):

    def test_sanitize_input_whitespace(self):
        """Verify that leading/trailing whitespaces, tabs, and newlines are stripped."""
        self.assertEqual(sanitize_input("  paris  "), "paris")
        self.assertEqual(sanitize_input("\tparis\n"), "paris")
        self.assertEqual(sanitize_input("paris"), "paris")

    def test_sanitize_input_case(self):
        """Verify that input capitalizations are neutralized to lowercase."""
        self.assertEqual(sanitize_input("Paris"), "paris")
        self.assertEqual(sanitize_input("PARIS"), "paris")
        self.assertEqual(sanitize_input("pArIs"), "paris")

    def test_sanitize_input_combined(self):
        """Verify that case neutralization and whitespace stripping work in combination."""
        self.assertEqual(sanitize_input("  \t PaRiS \n  "), "paris")

    def test_evaluate_answer_correct(self):
        """Ensure correct answers evaluate to True regardless of casing or whitespace."""
        self.assertTrue(evaluate_answer("Paris", "paris"))
        self.assertTrue(evaluate_answer("  paris  ", "paris"))
        self.assertTrue(evaluate_answer("PARIS", "paris"))
        self.assertTrue(evaluate_answer("mars", "mars"))
        self.assertTrue(evaluate_answer("  Mars\t", "mars"))

    def test_evaluate_answer_incorrect(self):
        """Ensure incorrect answers evaluate to False."""
        self.assertFalse(evaluate_answer("london", "paris"))
        self.assertFalse(evaluate_answer("p aris", "paris"))  # Internal spaces are preserved
        self.assertFalse(evaluate_answer("", "paris"))
        self.assertFalse(evaluate_answer("jupiter", "mars"))

if __name__ == "__main__":
    unittest.main()
