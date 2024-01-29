import unittest
from main import question_asker

class TestFunction(unittest.TestCase):
    def test_question_asker(self):
        expected = "Good!"
        result = question_asker("How is today going?")

        assert(expected, result)