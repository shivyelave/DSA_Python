'''


    @Author: Shivraj Yelave
    @Date: 30-07-24
    @Last modified by: Shivraj Yelave
    @Last modified time:
    @Title: Extract Unique Values from Dictionary


'''

def unique_values(input_list):

    """
    
    Description:
        Function to extract unique values from a list of dictionaries. 

    Parameters:
        input_list (list): The input list containing dictionaries from which to extract unique values.

    Returns:
        set: A set containing unique values from the dictionaries.
    
    """
    
    values = []  # Initialize an empty list to store values

    # Iterate through each dictionary in the list
    for dictionary in input_list:
        # Extract values from the current dictionary
        value_list = list(dictionary.values())
        # Append these values to the values list
        values.extend(value_list)
  
    # Convert the values list to a set to remove duplicates and return the unique values
    return set(values)

def main():
    # Define a sample list of dictionaries
    dictionary_list = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]

    # Call the function to extract unique values and print the result
    print(f"Unique values: {unique_values(dictionary_list)}")

# If this script is run as the main module, execute the main function
if __name__ == '__main__':
    main()
