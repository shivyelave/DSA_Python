'''


    @Author: Shivraj Yelave
    @Date: 26-02-24
    @Last modified by: Shivraj Yelave
    @Last modified time:
    @Title: Plot histogram of given data.

    
'''

# Importing necessary library
import matplotlib.pyplot as plt

def create_histogram(data,  num_bins=10):
    """
    Description:
    Function to create and display a histogram from a given list of integers.

    Parameters:
    data : A list of integers to generate the histogram from.
    bin_range : A tuple specifying the lower and upper range of the bins (optional).
    num_bins : The number of bins to use in the histogram (default is 10).

    Returns:
    None
    """
    # Creating the histogram with specified bins and range
    plt.hist(data, bins=num_bins,edgecolor='black')

    # Adding a title to the histogram
    plt.title('Histogram of Given Data')
    plt.xlabel('Value')
    plt.ylabel('Frequency')

    # Displaying the histogram
    plt.show()


def main():
    # Sample data: a list of integers
    data = [13,23,42,12,54,67,97,96,45,12,34,54,23,53,65]
    # Specifying the number of bins
    num_bins = 5
    create_histogram(data, num_bins=num_bins)

# Example usage
if __name__ == "__main__":
    main()