'''


    @Author: Shivraj Yelave
    @Date: 28-07-24
    @Last modified by: Shivraj Yelave
    @Last modified time:
    @Title: Sort List Based on Last Element of Tuples


'''
def sort_list_based_on_last_element_of_tuples(tuples_list):

    '''
    Description:
        This function sorts a list of tuples based on the last element of each tuple in descending order using selection sort.

    Parameters:
        tuples_list : list : the list of tuples to be sorted.

    Returns:
        list : the sorted list of tuples.
    '''
    
    n = len(tuples_list)
    for i in range(n):
        max_index = i
        for j in range(i + 1, n):
            if tuples_list[j][-1] > tuples_list[max_index][-1]:
                max_index = j
        # Swap the found maximum element with the first element
        tuples_list[i], tuples_list[max_index] = tuples_list[max_index], tuples_list[i]
    return tuples_list

def main():
    # Example list of tuples
    tuples_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
    
    # Sort the list based on the last element of each tuple in descending order
    sorted_tuples = sort_list_based_on_last_element_of_tuples(tuples_list)
    
    # Print the sorted list
    print("Sorted list of tuples based on the last element (largest first):")
    print(sorted_tuples)

if __name__ == '__main__':
    # Call the main function when the script is executed
    main()
