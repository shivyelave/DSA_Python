'''

    @Author: Shivraj Yelave
    @Date: 29-07-24
    @Last modified by: Shivraj Yelave
    @Last modified time:
    @Title: Add Members to a Set

'''

def add_members(input_set, *args):
    """
    Description:
    Function to add multiple members to a set.

    Parameters:
    input_set (set): The original set to which members will be added.
    *args: Members to be added to the set.

    Returns:
    set: The updated set with new members added.
    """
    for member in args:  # Iterate over each member in args
        input_set.add(member)  # Add each member to the set

    return input_set  # Return the updated set

def main():
    input_set = {2, 3, 4, 5, 6}  # Sample input set
    member1 = 6
    member2 = 7
    member3 = 8
    print(f"Set after adding members: {add_members(input_set, member1, member2, member3)}")

# If this script is run as the main module, execute the main function
if __name__ == '__main__':
    main()
