import unittest
from functions.get_files_info import get_files_info

class TestFunctions(unittest.TestCase):
    def test_root(self):
        result = get_files_info("calculator", ".")
        self.assertEqual(result, "- main.py: file_size=575 bytes, is_dir=False\n- tests.py: file_size=1342 bytes, is_dir=False\n- pkg: file_size=7772 bytes, is_dir=True")
        print(result)

    def test_pkg(self):
        result = get_files_info("calculator", "pkg")
        self.assertEqual(result, "- __pycache__: file_size=5269 bytes, is_dir=True\n- calculator.py: file_size=1737 bytes, is_dir=False\n- render.py: file_size=766 bytes, is_dir=False")
        print(result)

    def test_nonexistent_directory(self):
        result = get_files_info("calculator", "/bin")
        self.assertEqual(result, 'Error: "/bin" is not a directory')
        print(result)

    def test_directory_outside_of_working_directory(self):
        result = get_files_info("calculator", "../")
        self.assertEqual(result, 'Error: Cannot list "../" as it is outside the permitted working directory')
        print(result)

if __name__ == "__main__":
    unittest.main()