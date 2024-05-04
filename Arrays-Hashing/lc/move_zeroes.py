# Submitted solution
# Time complexity: O(n^2) due to the use of pop() method which takes O(n) time
# Space complexity: O(1) as we are not using any extra space

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = 0 
        n = len(nums)

        while i < n:
            if nums[i] == 0:
                nums.pop(i) # Remove the 0 
                nums.append(0) # Append 0 to the end
                n -= 1 # Decrement the length of the array
                continue
            i += 1
    

# Optimized solution
# Time complexity: O(n) as we are iterating through the array only once
# We do so by making use of two pointers:
# One pointer to iterate through the array and another pointer to 
# keep track of the position where we need to place the next non-zero element

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        zero_pointer = 0

        for i in range(n):
            # When encountering a non-zero element, swap it with the zero_pointer element
            if nums[i] != 0:
                nums[i], nums[zero_pointer] = nums[zero_pointer], nums[i] # In-place swap
                zero_pointer += 1