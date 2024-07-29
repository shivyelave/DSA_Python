'''


    @Author: Shivraj Yelave
    @Date: 29-07-24
    @Last modified by: Shivraj Yelave
    @Last modified time:
    @Title: permute the list
    

'''

def permute(lst):

    """
    
    Description:
    Function to generate all permutations of a list using recursion.

    Parameters:
    lst (list): The input list to permute.

    Returns:
    list: A list of lists, where each sublist is a permutation of the input list.

    """

    def _permute(current, remaining):
        if not remaining:
            permutations.append(current)
        else:
            for i in range(len(remaining)):
                new_current = current + [remaining[i]]
                new_remaining = remaining[:i] + remaining[i+1:]
                _permute(new_current, new_remaining)

    permutations = []
    _permute([], lst)
    return permutations

def main():
    lst = [1, 2, 3]  # Sample list
    perms = permute(lst)
    
    # Print all permutations
    print("All permutations of the list:")
    for perm in perms:
        print(perm)

# If this script is run as the main module, execute the main function
if __name__ == '__main__':
    main()
