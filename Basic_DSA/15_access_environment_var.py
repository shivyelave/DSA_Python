'''


    @Author: Shivraj Yelave
    @Date: 26-02-24
    @Last modified by: Shivraj Yelave
    @Last modified time:
    @Title: Access Environment Variables

    
'''

import os

def access_environment_variables(variable_name):
    """
    Description:
    Function to access and print the specified environment variable and all environment variables.

    Parameters:
    variable_name (str): The name of the environment variable to access.

    Returns:
    None
    """
    variable_value = os.getenv(variable_name)
    return variable_value

def main():
    variable_name = 'TEMP'
    variable_value = access_environment_variables(variable_name)
    print(f"{variable_name}: {variable_value}")


if __name__ == "__main__":
    main()

