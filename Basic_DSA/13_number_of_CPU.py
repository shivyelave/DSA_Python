'''

    @Author: Shivraj Yelave
    @Date: 26-02-24
    @Last modified by: Shivraj Yelave
    @Last modified time:
    @Title: Find the Number of CPUs

'''

import os

def find_number_of_cpus():
    """
    Description:
    Function to find and print the number of CPUs.

    Parameters:
    None

    Returns:
    None
    """
    num_cpus = os.cpu_count()
    print(f"Number of CPUs: {num_cpus}")

def main():
    find_number_of_cpus()

if __name__ == "__main__":
    main()
