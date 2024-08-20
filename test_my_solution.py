import unittest
from unittest.mock import patch, mock_open
from io import StringIO
import sys
from my_solution import extract_ids

class TestExtractIds(unittest.TestCase):

    def setUp(self):
        self.saved_stdout = sys.stdout
        sys.stdout = self.output = StringIO()

    def tearDown(self):
        sys.stdout = self.saved_stdout

    def testValidInput(self):
        test_data = "id1_1 1000\nid2_1 2000\nid3_1 3000\n"
        with patch("builtins.open", mock_open(read_data=test_data)):
            extract_ids("dummy_path", 2)
            output = self.output.getvalue().strip().split("\n")
            self.assertEqual(set(output), {"id3_1", "id2_1"})

    def testInvalidValue(self):
        test_data = "id1_1 1000\nid2_1 abc\nid3_1 3000\n"
        with patch("builtins.open", mock_open(read_data=test_data)):
            extract_ids("dummy_path", 2)
            output = self.output.getvalue().strip().split("\n")
            expected_output = {"id3_1", "id1_1", "line number 2 is not integer value = id2_1 abc"}
            self.assertEqual(set(output), expected_output)

    def testExtraValueAdded(self):
        test_data = "id1_1 1000\nid2_1 2000 extra\nid3_1 3000\n"
        with patch("builtins.open", mock_open(read_data=test_data)):
            extract_ids("dummy_path", 2)
            output = self.output.getvalue().strip().split("\n")
            # Include the warning message in the expected output
            expected_output = {"id3_1", "id1_1", "line number 2 is not in pattern unique_id and an value = id2_1 2000 extra"}
            self.assertEqual(set(output), expected_output)

    def testEmptyLine(self):
        test_data = "id1_1 1000\n\nid3_1 3000\n"
        with patch("builtins.open", mock_open(read_data=test_data)):
            extract_ids("dummy_path", 2)
            output = self.output.getvalue().strip().split("\n")
            expected_output = {"id3_1", "id1_1", "line number 2 is empty"}
            self.assertEqual(set(output), expected_output)

    def testInvalidN(self):
        test_data = "id1_1 1000\nid2_1 2000\nid3_1 3000\n"
        with patch("builtins.open", mock_open(read_data=test_data)):
            extract_ids("dummy_path", 0)
            output = self.output.getvalue().strip()
            self.assertEqual(output, "Number must be positive integer")
            
            self.output.truncate(0)
            self.output.seek(0)

            extract_ids("dummy_path", -1)
            output = self.output.getvalue().strip()
            self.assertEqual(output, "Number must be positive integer")

    def testNGreaterThanLine(self):
        test_data = "id1_1 1000\nid2_1 2000\n"
        with patch("builtins.open", mock_open(read_data=test_data)):
            extract_ids("dummy_path", 5)
            output = self.output.getvalue().strip().split("\n")
            self.assertEqual(set(output), {"id2_1", "id1_1"})

    def testFileWithNoInvalidData(self):
        test_data = "\nabc\nid2_1 abc\n"
        with patch("builtins.open", mock_open(read_data=test_data)):
            extract_ids("dummy_path", 2)
            output = self.output.getvalue().strip().split("\n")
            expected_output = [
                "line number 1 is empty",
                "line number 2 is not in pattern unique_id and an value = abc",
                "line number 3 is not integer value = id2_1 abc",
                "no valid data found in the input file"
            ]
            self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()
