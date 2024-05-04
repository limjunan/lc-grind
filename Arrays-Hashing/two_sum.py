
# Two pointer implementation
class Solution(object):
    def twoSum(self, nums, target):
        sorted_nums_indices = sorted(range(len(nums)), key=lambda k: nums[k])
        p1 = 0
        p2 = len(nums) - 1

        while p1 < p2:
            if nums[sorted_nums_indices[p1]] + nums[sorted_nums_indices[p2]] == target:
                return [sorted_nums_indices[p1], sorted_nums_indices[p2]]
            elif nums[sorted_nums_indices[p1]] + nums[sorted_nums_indices[p2]] < target:
                p1 += 1
            else:
                p2 -= 1

# Dictionary Implementation
class Solution2(object):
    def twoSum(self, nums, target):
        num_to_index = {}
        
        for i, num in enumerate(nums):
            if target - num in num_to_index:
                return [num_to_index[target - num], i]
            num_to_index[num] = i