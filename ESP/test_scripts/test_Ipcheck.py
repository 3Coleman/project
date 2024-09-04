import unittest
import subprocess
import os

class TestIpCheck(unittest.TestCase):
    Generator_Script=r'C:\Abel\project\ESP\test_scripts\ESP32.PY'
    File_Path="serial_log.txt"
    search_string='WiFi'
    
    def Verify_Python_file(self):
        try:
            result=subprocess.run(
                ['python',self.Generator_Script],capture_output=True,text=True,check=True
            )
            print(result.stdout)
        except subprocess.CalledProcessError as e:
            self.fail(f"failed to run generator script:{e.stderr.strip()}")
    
    def verify_string_in_file(self):
        if not os.path.isfile(self.File_Path):
            self.fail(f"file{self.File_PATH} isn't exists")
        with open(self.File_Path,'r') as f:
            for line in f :
                if self.search_string in line:
                    return
        self.fail(f"the searching value{self.serach_string} isnt found in the log")

    def test_verify(self):
        self.Verify_Python_file()
        self.verify_string_in_file()

    def tearDown(self):
        if os.path.isfile(self.File_Path):
            os.remove(self.File_Path)

if __name__=='__main__':
    unittest.main()





        
