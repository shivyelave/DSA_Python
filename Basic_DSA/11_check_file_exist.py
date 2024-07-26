'''

    @Author: Shivraj Yelave
    @Date: 26-02-24
    @Last modified by: Shivraj Yelave
    @Last modified time:
    @Title: Check Whether a File Exists

'''

import os

def check_file_exists(path):
    """
    Description:
    Function to check if a file exists at the specified path.

    Parameters:
    file_path (str): The path to the file.

    Returns:
    None
    """
    if os.path.isfile(path):
        print(f"The file '{path}' exists.")
    else:
        print(f"The file '{path}' does not exist.")

def main():
    file_path = 'C:/Users/Admin/Documents/Python Basics/DSA/Basic_python/12_cl_external_command.py'
    check_file_exists(file_path)

if __name__ == "__main__":
    main()
