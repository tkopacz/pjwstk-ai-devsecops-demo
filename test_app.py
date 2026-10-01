import unittest

from app import classify


class ClassifierTests(unittest.TestCase):
    def test_password(self):
        self.assertEqual(classify("Reset password", "SYNTHETIC-1")["queue"], "IT")

    def test_general(self):
        self.assertEqual(classify("Opening hours", "SYNTHETIC-2")["queue"], "GENERAL")

    def test_missing_source(self):
        self.assertEqual(classify("Reset password", " ")["decision"], "BLOCK")

    def test_empty(self):
        self.assertEqual(classify(" ", "SYNTHETIC-1")["decision"], "BLOCK")


if __name__ == "__main__":
    unittest.main()