import unittest
from unittest.mock import patch, mock_open
from io import StringIO
import sys
import logging
from my_solution import extract_top_n_ids

class TestExtractTopNIds(unittest.TestCase):

    def setUp(self):
        self.saved_stdout = sys.stdout
        sys.stdout = self.output = StringIO()

    def tearDown(self):
        sys.stdout = self.saved_stdout

    @patch('my_solution.logging')
    def test_valid_input(self, mock_logging):
        test_data = "id1_1 1000\nid2_1 2000\nid3_1 3000\n"
        with patch("builtins.open", mock_open(read_data=test_data)):
            extract_top_n_ids("dummy_path", 2)
            output = self.output.getvalue().strip().split("\n")
            self.assertEqual(set(output), {"id3_1", "id2_1"})

    @patch('my_solution.logging')
    def test_invalid_value(self, mock_logging):
        test_data = "id1_1 1000\nid2_1 abc\nid3_1 3000\n"
        with patch("builtins.open", mock_open(read_data=test_data)):
            extract_top_n_ids("dummy_path", 2)
            output = self.output.getvalue().strip().split("\n")
            expected_output = {"id3_1", "id1_1"}
            self.assertEqual(set(output), expected_output)
            mock_logging.error.assert_called_with("Line 2 not a integer value : 'abc'.")

    @patch('my_solution.logging')
    def test_extra_value_added(self, mock_logging):
        test_data = "id1_1 1000\nid2_1 2000 extra\nid3_1 3000\n"
        with patch("builtins.open", mock_open(read_data=test_data)):
            extract_top_n_ids("dummy_path", 2)
            output = self.output.getvalue().strip().split("\n")
            expected_output = {"id3_1", "id1_1"}
            self.assertEqual(set(output), expected_output)
            mock_logging.warning.assert_called_with("Line 2 is invalid form : 'id2_1 2000 extra'.")

    @patch('my_solution.logging')
    def test_empty_line(self, mock_logging):
        test_data = "id1_1 1000\n\nid3_1 3000\n"
        with patch("builtins.open", mock_open(read_data=test_data)):
            extract_top_n_ids("dummy_path", 2)
            output = self.output.getvalue().strip().split("\n")
            expected_output = {"id3_1", "id1_1"}
            self.assertEqual(set(output), expected_output)
            mock_logging.warning.assert_called_with("Line 2 is empty.")

    @patch('my_solution.logging')
    def test_invalid_n(self, mock_logging):
        test_data = "id1_1 1000\nid2_1 2000\nid3_1 3000\n"
        with patch("builtins.open", mock_open(read_data=test_data)):
            extract_top_n_ids("dummy_path", 0)
            mock_logging.error.assert_called_with("Number of ids to extract must be a positive integer.")
            self.output.truncate(0)
            self.output.seek(0)
            extract_top_n_ids("dummy_path", -1)
            mock_logging.error.assert_called_with("Number of ids to extract must be a positive integer.")

    @patch('my_solution.logging')
    def test_n_greater_than_lines(self, mock_logging):
        test_data = "id1_1 1000\nid2_1 2000\n"
        with patch("builtins.open", mock_open(read_data=test_data)):
            extract_top_n_ids("dummy_path", 5)
            output = self.output.getvalue().strip().split("\n")
            self.assertEqual(set(output), {"id2_1", "id1_1"})

    @patch('my_solution.logging')
    def test_file_with_no_valid_data(self, mock_logging):
        test_data = "\nabc\nid2_1 abc\n"
        with patch("builtins.open", mock_open(read_data=test_data)):
            extract_top_n_ids("dummy_path", 2)
            mock_logging.warning.assert_any_call("Line 1 is empty.")
            mock_logging.warning.assert_any_call("Line 2 is invalid form : 'abc'.")
            mock_logging.error.assert_any_call("Line 3 not a integer value : 'abc'.")
            mock_logging.error.assert_called_with("No valid data in this file.")

    @patch('my_solution.logging')
    def test_large_input(self, mock_logging):
        test_data = "\n".join(f"id{i} {i * 1000}" for i in range(1, 10001))
        with patch("builtins.open", mock_open(read_data=test_data)):
            extract_top_n_ids("dummy_path", 5)
            output = self.output.getvalue().strip().split("\n")
            expected_output = {f"id9999", f"id10000", f"id9998", f"id9997", f"id9996"}
            self.assertEqual(set(output), expected_output)

    @patch('my_solution.logging')
    def test_file_not_found(self, mock_logging):
        with patch("builtins.open", side_effect=FileNotFoundError):
            extract_top_n_ids("non_existent_file.txt", 5)
            mock_logging.error.assert_called_with("File not found : non_existent_file.txt")

if __name__ == '__main__':
    unittest.main()
