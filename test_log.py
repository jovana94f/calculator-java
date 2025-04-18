import unittest
from unittest.mock import patch, mock_open
import os
from log import calculate_loc_for_java_files

class TestCalculateLocForJavaFiles(unittest.TestCase):
    @patch("os.walk")
    @patch("builtins.open", new_callable=mock_open, read_data="public class Test {} // comment\n\n")
    def test_multiple_java_files(self, mock_file, mock_walk):
        # Mock directory structure with multiple .java files
        mock_walk.return_value = [
            ("/mock_dir", ("subdir",), ("File1.java", "File2.java")),
            ("/mock_dir/subdir", (), ("File3.java",)),
        ]
        loc_data, total_loc = calculate_loc_for_java_files("/mock_dir")
        self.assertEqual(loc_data, {"File1.java": 1, "File2.java": 1, "File3.java": 1})
        self.assertEqual(total_loc, 3)

    @patch("os.walk")
    def test_no_java_files(self, mock_walk):
        # Mock directory structure with no .java files
        mock_walk.return_value = [
            ("/mock_dir", ("subdir",), ("File1.txt", "File2.py")),
        ]
        loc_data, total_loc = calculate_loc_for_java_files("/mock_dir")
        self.assertEqual(loc_data, {})
        self.assertEqual(total_loc, 0)

    @patch("os.walk")
    @patch("builtins.open", new_callable=mock_open, read_data="public class Test {}")
    def test_nested_directories(self, mock_file, mock_walk):
        # Mock nested directory structure with .java files
        from calculator import calculate  # Assuming the calculator function is in calculator.py

        class TestCalculator(unittest.TestCase):
            def test_simple_addition(self):
                self.assertEqual(calculate("2+3"), 5)

            def test_mixed_operations(self):
                self.assertEqual(calculate("10+5*4-3"), 27)

            def test_parentheses(self):
                self.assertEqual(calculate("(2+3)*4"), 20)

            def test_division(self):
                self.assertEqual(calculate("10/2"), 5.0)

            def test_invalid_expression(self):
                with self.assertRaises(SyntaxError):
                    calculate("2++3")
                    from calculator import calculate  # Assuming the calculator function is in calculator.py

                    class TestCalculateLocForJavaFiles(unittest.TestCase):
                        @patch("os.walk")
                        @patch("builtins.open", new_callable=mock_open, read_data="public class Test {} // comment\n\n")
                        def test_multiple_java_files(self, mock_file, mock_walk):
                            mock_walk.return_value = [
                                ("/mock_dir", ("subdir",), ("File1.java", "File2.java")),
                                ("/mock_dir/subdir", (), ("File3.java",)),
                            ]
                            loc_data, total_loc = calculate_loc_for_java_files("/mock_dir")
                            self.assertEqual(loc_data, {"File1.java": 1, "File2.java": 1, "File3.java": 1})
                            self.assertEqual(total_loc, 3)

                        @patch("os.walk")
                        def test_no_java_files(self, mock_walk):
                            mock_walk.return_value = [
                                ("/mock_dir", ("subdir",), ("File1.txt", "File2.py")),
                            ]
                            loc_data, total_loc = calculate_loc_for_java_files("/mock_dir")
                            self.assertEqual(loc_data, {})
                            self.assertEqual(total_loc, 0)

                        @patch("os.walk")
                        @patch("builtins.open", new_callable=mock_open, read_data="public class Test {}")
                        def test_nested_directories(self, mock_file, mock_walk):
                            mock_walk.return_value = [
                                ("/mock_dir", ("subdir",), ("File1.java",)),
                                ("/mock_dir/subdir", (), ("File2.java",)),
                            ]
                            loc_data, total_loc = calculate_loc_for_java_files("/mock_dir")
                            self.assertEqual(loc_data, {"File1.java": 1, "File2.java": 1})
                            self.assertEqual(total_loc, 2)

                    class TestCalculator(unittest.TestCase):
                        def test_simple_addition(self):
                            self.assertEqual(calculate("2+3"), 5)

                        def test_mixed_operations(self):
                            self.assertEqual(calculate("10+5*4-3"), 27)

                        def test_parentheses(self):
                            self.assertEqual(calculate("(2+3)*4"), 20)

                        def test_division(self):
                            self.assertEqual(calculate("10/2"), 5.0)

                        def test_invalid_expression(self):
                            with self.assertRaises(SyntaxError):
                                calculate("2++3")

                        def test_empty_expression(self):
                            with self.assertRaises(ValueError):
                                calculate("")

                        def test_large_numbers(self):
                            self.assertEqual(calculate("1000000*1000000"), 1000000000000)

                        def test_subtraction(self):
                            self.assertEqual(calculate("10-3"), 7)

                        def test_combined_operations(self):
                            self.assertEqual(calculate("10/2+3*4-1"), 15.0)

                        def test_invalid_characters(self):
                            with self.assertRaises(ValueError):
                                calculate("10+abc")

                    if __name__ == "__main__":
                        with open("TEST-RESULTS", "w") as results_file:
                            runner = unittest.TextTestRunner(results_file, verbosity=2)
                            unittest.main(testRunner=runner)
