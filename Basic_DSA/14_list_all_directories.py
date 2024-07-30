'''

    @Author: Shivraj Yelave
    @Date: 26-02-24
    @Last modified by: Shivraj Yelave
    @Last modified time:
    @Title: List All Files in a Directory

'''

import os

def list_files_in_directory(directory_path):
    """
    Description:
    Function to list all files in the specified directory.

    Parameters:
    directory_path (str): The path to the directory.

    Returns:
    all files in that directory
    """
    try:
        files = os.listdir(directory_path)
        return files

    except FileNotFoundError:
        print(f"The directory '{directory_path}' does not exist.")

def main():
    directory_path = 'C:/Users/Admin/Documents/Python Basics/DSA/Basic_python'
    files = list_files_in_directory(directory_path)
    print(f"Files in '{directory_path}':")
    for file in files:
        print(file)

if __name__ == "__main__":
    main()
