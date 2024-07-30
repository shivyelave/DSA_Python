def count_keys_have_specific_value(list_dictionary,key,value):
    count = 0
    for dictionary in list_dictionary:
        if dictionary[key]==value:
            count += 1
    return count
def main():
    list_dict =  [{'id': 1, 'success': True, 'name': 'Lary'}, {'id': 2, 'success':False, 'name': 'Rabi'}, {'id': 3, 'success': True, 'name': 'Alex'}]
    key = 'success'
    value =False
    print(f"Dictionary have {key} value {value} {count_keys_have_specific_value(list_dict,key,value)} times.")

if __name__ == '__main__':
    main()