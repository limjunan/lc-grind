# Python list as an array
arr = [1, 2, 3, 4, 5]

# Useful techniques in arrays

# 1. Reversing an array
arr.reverse()

# 2. Sorting an array
arr.sort(reverse=False) # Ascending order
sorted_arr = sorted(arr, reverse=False)
# Note: sort() method sorts the array in place, while sorted() method returns a new sorted array

# 3. Slicing an array
arr[1:3] # Gets the 1st index (inclusive) and 3rd index (exclusive) of the array [2, 3]

# 4. Copying an array
arr2 = arr.copy() # Shallow copy

# 5. Merging two arrays
arr3 = arr + arr2

# Useful Leetcode Techniques

# 1. List comprehension to create an array
squares = [i**2 for i in arr] # [1, 4, 9, 16, 25]

# 2. map() - apply a function to all the elements of an array
squares_map = list(map(lambda x: x**2, arr)) # [1, 4, 9, 16, 25]

# 3. filter() - filter elements of an array
even = list(filter(lambda x: x % 2 == 0, arr)) # [2, 4]

# 4. Two pointer technique - useful for finding pairs in an array
# Note: array should be sorted
def two_sum(arr, target):
    left, right = 0, len(arr) - 1
    while left < right:
        if arr[left] + arr[right] == target:
            return [left, right]
        elif arr[left] + arr[right] < target:
            left += 1
        else:
            right -= 1
    return [-1, -1]