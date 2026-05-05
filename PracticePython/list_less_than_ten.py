""" takes in a list and prints out the nums in the list that are less than 5"""

def less_than_five(number_list:list):
    """ takes in list of nums and prints out those < 5"""
    nums_less_than_five = []
    for num in number_list:
        if num < 5:
            nums_less_than_five.append(num)

    print(nums_less_than_five)

less_than_five([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89])
