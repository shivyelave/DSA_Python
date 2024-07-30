def is_circular_identical(list1,list2):
    if len(list1)== len(list2):
        temp = list2
        for index in range(len(list1)):
            list2 = temp
            list2 = list2[index:]+list2[:index]
            if list1 == list2:
                return True
        else:
            return False
    else:
        return False
def main():
    list1= [1, 2, 3, 4]
    list2= [3, 4, 1, 2]
    print(is_circular_identical(list1,list2))
if __name__ == '__main__':
    # Call the main function when the script is executed
    main()