import os
import random
import string

def create_junk_file(file_path, size=1024):
    """Create a file with random junk data of a specified size."""
    # Generate random junk data
    junk_data = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=size))
    
    # Write junk data to the file
    with open(file_path, 'w') as f:
        f.write(junk_data)
    
    print(f"File created at {file_path} with {size} bytes of junk data.")

if __name__ == '__main__':
    file_path = 'junk_file.txt'
    create_junk_file(file_path)
