'''

    @Author: Shivraj Yelave
    @Date: 27-07-24
    @Last modified by: Shivraj Yelave
    @Last modified time:
    @Title: Format Paragraph Text to a Specified Width

'''

def display_formatted_text(paragraph, width):
    """
    Description:
    Function to format a paragraph so that each line of the output does not exceed the specified width.

    Parameters:
    paragraph (str): The input paragraph to format.
    width (int): The maximum number of characters per line.

    Returns:
    str: The formatted paragraph with lines of specified width.
    """
    formatted_string = ''  # Initialize an empty string to hold the formatted text
    line_length = 0  # Track the current length of the line

    # Loop through each character in the paragraph
    for letter in paragraph:
        # Check if adding the next character would exceed the specified width
        if line_length == width:
            # If so, add a newline character to start a new line
            formatted_string += '\n'
            line_length = 0  # Reset the line length counter
        
        # Append the current character to the formatted string
        formatted_string += letter
        line_length += 1  # Increment the line length counter

    return formatted_string

def main():
    paragraph = "In the bustling world of technology, few innovations have had as profound an impact on our daily lives as the advent of the internet. This revolutionary tool has transformed communication, commerce, and entertainment in ways previously unimaginable. From the early days of dial-up connections to the high-speed fiber optics of today, the internet has continually evolved, reshaping how we interact with information and each other. One of the most significant changes brought about by the internet is the rise of social media platforms. These platforms have created virtual communities where people from across the globe can connect, share ideas, and collaborate on projects. This interconnectedness has not only facilitated personal relationships but has also played a crucial role in social movements and political activism. Additionally, the internet has revolutionized the way we consume media. Streaming services have replaced traditional television and radio, providing on-demand access to a vast array of content. This shift has altered the entertainment industry, leading to the rise of digital content creators and a more personalized viewing experience. E-commerce has also seen tremendous growth, with online shopping becoming a preferred method for purchasing goods and services. The convenience of shopping from home, coupled with the vast selection of products available at our fingertips, has changed consumer behavior and led to the decline of many brick-and-mortar stores. However, the internet is not without its challenges. Issues such as cybersecurity, privacy concerns, and the digital divide highlight the need for ongoing vigilance and innovation. As technology continues to advance, it is crucial to address these challenges while harnessing the internet's potential to improve our lives. The internet remains a powerful tool that has transformed our world in countless ways, and its influence will undoubtedly continue to shape the future."
    width = 60  # Define the maximum width for each line
    # Call the display_formatted_text function with the sample paragraph and width, then print the result
    print(display_formatted_text(paragraph, width))

# If this script is run as the main module, execute the main function
if __name__ == '__main__':
    main()
