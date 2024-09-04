# test_generate_and_verify_junk_file.py
import unittest
import subprocess
import os

class TestGenerateAndVerifyJunkFile(unittest.TestCase):
    GENERATOR_SCRIPT = r'C:\Abel\project\ESP\test_scripts\ESP32.PY'
    FILE_PATH = 'serial_log.txt'
    SEARCH_STRING = 'WiFi IP'

    def run_generator_script(self):
        """Run the junk file generator script."""
        try:
            result = subprocess.run(['python', self.GENERATOR_SCRIPT], capture_output=True, text=True, check=True)
            print(result.stdout)  # Print output from the generator script
        except subprocess.CalledProcessError as e:
            self.fail(f"Failed to run generator script: {e.stderr.strip()}")

    def verify_string_in_file(self):
        """Check if the specific string is in the generated junk file."""
        if not os.path.exists(self.FILE_PATH):
            self.fail(f"File {self.FILE_PATH} does not exist.")

        with open(self.FILE_PATH, 'r') as f:
            content = f.read()

        self.assertIn(self.SEARCH_STRING, content, f"String '{self.SEARCH_STRING}' not found in file content.")

    def test_generate_and_verify_junk_file(self):
        """Test that the junk file contains the specific string after generation."""
        self.run_generator_script()
        self.verify_string_in_file()

    def tearDown(self):
        """Remove the generated junk file after each test."""
        if os.path.exists(self.FILE_PATH):
            os.remove(self.FILE_PATH)

if __name__ == '__main__':
    unittest.main()
