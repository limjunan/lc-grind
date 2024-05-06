# Submitted Solution 1
# A little more optimized brute force method
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) < k or k == 1:
            return nums

        output = [max(nums[:k])]
        maxIndex = -1
        maxNum = 0

        for i in range(k, len(nums)):
            if nums[i] < maxNum and maxIndex >= i - k + 1:
                output.append(maxNum)
                continue
            elif nums[i] >= maxNum and maxIndex >= i - k + 1: 
                maxNum = nums[i]
                maxIndex = i
                output.append(maxNum)
            else:
                maxNum = max(nums[i-k+1:i+1])
                maxIndex = nums[i-k+1:i+1].index(maxNum)
                output.append(max(nums[i-k+1:i+1]))

        return output
    
# Submitted Solution 2
# Using deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return [max(nums)]
        
        q = collections.deque()
        output = []
        l, r = 0, 0

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if l > q[0]:
                q.popleft()

            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1

            r += 1

        return output
    