class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        a = 0
        output = []

        # Iterate through the array until we reach 0 as we need a negative number to make 0
        while a < len(nums) and nums[a] <= 0:

            # Skip the duplicates
            if a > 0 and nums[a] == nums[a - 1]:
                a += 1
                continue

            p1 = a + 1
            p2 = len(nums) - 1
            target = 0 - nums[a]
            
            # Basically two sum pointer approach
            while p2 > p1:
                if((nums[p2] + nums[p1]) > target):
                    p2 -= 1
                elif((nums[p2] + nums[p1]) < target):
                    p1 += 1
                else:
                    thriplet = [nums[a], nums[p1], nums[p2]]
                    output.append(thriplet)
                    p1 += 1

                    # Skip the duplicates
                    while(nums[p1] == nums[p1 - 1] and p2 > p1):
                        p1 += 1

            a += 1

        return output
        