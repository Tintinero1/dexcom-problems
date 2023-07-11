# Problem 1
# Given an integer list nums, write a function that solves the following problem; return true if
# any value appears at least twice in the list, and return false if every element is distinct.
# Example 1:
# Input: nums = [1,2,3,1]
# Output: true
# Example 2:
# Input: nums = [1,2,3,4]
# Output: false
# Example 3:
# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true


# SOLUTION:
# We can create a hashmap to keep track of the times that we see an integer in the list
# assigning a counter value each time we see a new integer. Once we see that integer
# again, we know that we can return False becuase that element is duplicated
# according to our hashmap.

# SPECIAL CASES:
# Evaluating the length to 0, let us know if an empty list was provided hence returning False
# becuse no elements in list.

# EXCEPTIONS:
# If we found a value for nums different to a list we raise an exception. That way we cover non list values.
# If we found a value in nums different to an int we raise an exception. That way we cover non integer values.

# TIME AND SPACE COMPLEXITY:
# Time complexity: O(n)
# Why? Because we are traversing the for loop in a range of 'n' elements in list nums

# Space complexity: O(n)
# Why? Because the hashmap that we have grows depending on the list that we are traversing with 'n' elements

def check_duplicates(nums: list):
    if type(nums) != list:
        raise TypeError("nums must be a list")
    
    if len(nums) == 0:
        return False
    
    hash_map = {}
    for index in range(len(nums)):

        if type(nums[index]) != int:
            raise TypeError("nums value must be type int")
        if nums[index] in hash_map:
            return True
        else:
            hash_map[nums[index]] = 1

    return False
