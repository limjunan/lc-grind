class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        start, end = 0, len(nums) - 1

        while start <= end:
            middle = (start + end) // 2
            if nums[middle] == target: return middle

            if nums[middle] >= nums[start]:
                if target > nums[middle] or target < nums[start]: 
                    start = middle + 1
                else: end = middle - 1
            else:
                if target < nums[middle] or target > nums[end]: 
                    end = middle - 1
                else: start = middle + 1

        return -1