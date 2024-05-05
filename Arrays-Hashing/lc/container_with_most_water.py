# Submitted solution 1: brute force lol

class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height) == 2:
            return min(height[0], height[1])

        volume = [0, min(height[0], height[1])]
        for i in range(2, len(height)):
            volume.append(min(height[i], height[i - 1]))
            for j in range(1, len(volume)):
                volume[j] = max(volume[j], (i - j + 1) * min(height[j - 1], height[i]))
            
            print(volume)
        return max(volume)

# Submitted solution 2: Two pointer approach

class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height) == 2:
            return min(height[0], height[1])

        start, end = 0, len(height) - 1
        output = 0

        while end > start:
            print(start, end)
            volume = min(height[start], height[end]) * (end - start)
            output = max(output, volume)

            if height[start] < height[end]:
                start += 1
            else:
                end -= 1
        
        return output
# Submitted solution 3: Two pointer approach with optimization
class Solution:
    def MaxArea(self, height: List[int]) -> int:
        if len(height) == 2:
            return min(height[0], height[1])

        start, end = 0, len(height) - 1
        output = 0

        while end > start:
            volume = min(height[start], height[end]) * (end - start)
            output = max(output, volume)

            if height[start] < height[end]:
                start += 1
                # Skip the duplicates
                while height[start] < height[start - 1] and end > start:
                    start += 1
            else:
                end -= 1
                # Skip the duplicates
                while height[end] < height[end + 1] and end > start:
                    end -= 1
        
        return output