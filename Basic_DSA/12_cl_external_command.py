'''

    @Author: Shivraj Yelave
    @Date: 26-02-24
    @Last modified by: Shivraj Yelave
    @Last modified time:
    @Title: Call an External Command

'''

import subprocess

def call_external_command(command):

    """
        Description:
        Function to call an external command and print its output.

        Parameters:
        command (list): The command to execute as a list of strings.

        Returns:
        Result of command
    """

    result = subprocess.run(command, capture_output=True, text=True, shell=True)
    return result.stdout

def main():
    # Check the operating system
    command = ['dir']  
    print("Result:",call_external_command(command))

if __name__ == "__main__":
    main()
