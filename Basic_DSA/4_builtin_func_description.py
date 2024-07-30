'''

    @Author: Shivraj Yelave
    @Date: 25-02-24
    @Last modified by: Shivraj Yelave
    @Last modified time:
    @Title: Print Documentation of Built-in Function

'''
import inspect
def print_doc(func):
    '''
    Description:
        This function prints the documentation of a given built-in function.

    Parameters:
        func : function : the built-in function to print documentation for.

    Returns:
        None
    '''
    print(func.__doc__.strip())
    print(func,inspect.signature(func))

def main():
    # Print the documentation of the abs() function
    print_doc(abs)

if __name__ == '__main__':
    main()
