# Problem 2
# Given a sorted list of distinct integers and a target value, write a function that solves the
# following problem; return the index if the target is found. If not, return the index where it
# would be if it were inserted in order.
# Example 1:
# Input: nums = [1,3,5,6], target = 5
# Output: 2
# Example 2:
# Input: nums = [1,3,5,6], target = 2
# Output: 1
# Example 3:
# Input: nums = [1,3,5,6], target = 7
# Output: 4

# SOLUTION:
# We can use a binary search function to look in the list for the target provided and at the same time
# we keep track of the index that we need in case that we don't find the target in the list.
# This can be done using a while loop with a low and high variable. By calculating and constantly updating
# the low, mid and high values, the list can be traversed in O(log n) time. This is because we are cutting in half
# the quantity of elements that we are searching on.

# SPECIAL CASES:
# Evaluating the list length to zero can give us in constant time
# the index of the target in the special case that the list is empty.

# Evaluating the target to less than or equal to the first index of the list can give us in constant time
# the index of the target in the special case that the target is lower or equal to the first value of the list.

# Evaluating the target to greater than to the last index of the list can give us in constant time
# the index of the target in the special case that the target is greater than the last value of the list.

# Evaluating the target being equal to the last index of the list can give us in constant time
# the index of the target in the special case that the target is equal than the last value of the list.

# EXCEPTIONS:
# If we found a value for target different to an int we raise an exception. That way we cover non integer values.
# If we found a value for sorted_list different to a list we raise an exception. That way we cover non list values.
# If we found a value in the list different to an int we raise an exception. That way we cover non integer values.

# TIME AND SPACE COMPLEXITY:
# Time complexity: O(log n)
# Why? Because on each iteration we cut the number of items from which we have to search in half. Giving us O(log n) time.

# Space complexity: O(1)
# Why? Because we are just asigning variables on each iteration in a constant amount of space. 
# The space does not grows with this algorithm

def binary_search(sorted_list: list, target: int):
    if type(target) != int:
        raise TypeError("target must be an int")
    
    if type(sorted_list) != list:
        raise TypeError("sorted_list must be a list")
    
    if len(sorted_list) == 0:
        return 0
    
    low = 0
    high = len(sorted_list) - 1
    index_to_insert = 0

    if target <= sorted_list[low]:
        return 0
    elif target > sorted_list[high]:
        return high + 1
    elif target == sorted_list[high]:
        return high

    while low <= high:
        mid = (high + low) // 2

        if type(sorted_list[mid]) != int:
            raise TypeError("sorted_list value must be an int")
    
        if sorted_list[mid] < target:
            low = mid + 1
            index_to_insert = mid + 1
        elif sorted_list[mid] > target:
            high = mid - 1
            index_to_insert = mid
        elif sorted_list[mid] == target:
            return mid
    
    return index_to_insert
