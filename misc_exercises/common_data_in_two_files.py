## list comprehension?
## iterate a list, do some computations and produce another list

# # simple list comprehension
# numbers = [1,2,3]
# new_numbers = [num + 1 for num in numbers]
# print(new_numbers)

# # double nums
# doubled = [num*2 for num in range(1,5)]
# print(doubled)

# # uppercase names
# short_names = ['alex', 'beth', 'caroline', 'eleanor', 'Freddie']
# upper_case_names = [name.upper() for name in short_names if len(name) > 5]
# print(upper_case_names)


# # read files and print common numbers
def list_of_nums(file_path):
    """read filepath and return numbers as list

    Args:
        file_path (str): filepath 
    """
    with open(file_path) as file:
        return [int(line.strip()) for line in file.readlines()]

def common_nums_between_lists(list1, list2):
    """find common numbers in two lists

    Args:
        list1 (list): list1
        list2 (list): list2
    """
    return [num for num in list1 if num in list2]


file1_list_of_nums = list_of_nums('file1.txt')
file2_list_of_nums = list_of_nums('file2.txt')
common_nums = common_nums_between_lists(file1_list_of_nums, file2_list_of_nums)
print(common_nums)