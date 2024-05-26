class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        smallest = 1
        d = {}

        for i in nums:
            if i not in d:
                d[i] = 1
        
        while smallest in d:
            smallest += 1
        
        return smallest

        