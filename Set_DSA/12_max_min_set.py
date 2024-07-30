def max_min(input_set):
    """
    Description:
        Function to find the maximum and minimum values in a set.

    Parameters:
        input_set : set : The set from which to find the maximum and minimum values.

    Returns:
        tuple : A tuple containing the maximum and minimum values in the set.
    """
    # Convert the set to a list to access elements by index
    list_from_set = list(input_set)
    
    # Initialize max and min with the first element of the list
    max_val = list_from_set[0]
    min_val = list_from_set[0]

    # Iterate through each element in the list
    for element in list_from_set:
        if element > max_val:
            max_val = element
        if element < min_val:
            min_val = element

    return max_val, min_val

def main():
    input_set = {2, 3, 45, 6, 75, 43}  # Sample set with some elements
    # Call the max_min function and print the result
    max_val, min_val = max_min(input_set)
    print(f"Max value: {max_val}, Min value: {min_val}")

# If this script is run as the main module, execute the main function
if __name__ == '__main__':
    main()
