'''

    @Author: Shivraj Yelave
    @Date: 29-07-24
    @Last modified by: Shivraj Yelave
    @Last modified time:
    @Title: Slice Tuple

'''

def slice_tuple(input_tuple, start, end):
    """
    Description:
    Function to slice a tuple from the given start to end indices.

    Parameters:
    input_tuple (tuple): The input tuple to slice.
    start (int): The starting index (1-based).
    end (int): The ending index (1-based).

    Returns:
    tuple: The sliced portion of the tuple.
    """
    # Ensure the indices are within the valid range
    if start > 0 and end <= len(input_tuple):
        return input_tuple[start-1:end]  # Slice the tuple using 0-based indices
    else:
        return "Invalid start or end index"  # Return an error message for invalid indices

def main():
    tuple = (2, 12, 23, 34, 2, 41, 24, 76)  # Sample input tuple
    start = 5  # Starting index (1-based)
    end = 8  # Ending index (1-based)
    # Call the slice_tuple function and print the result
    print(f"Sliced tuple: {slice_tuple(tuple, start, end)}")

# If this script is run as the main module, execute the main function
if __name__ == '__main__':
    main()
