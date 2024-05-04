# Submitted solution
# Time complexity: O(n) as we are iterating through the intervals list twice
# Space complexity: O(1) as we are not using any extra space

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        # Edge case: If the intervals list is empty, return the newInterval
        if intervals == []:
            return [newInterval]
        
        # Get the start and end index of the interval to merge
        startMerge, endMerge = -1, -1
        for i in range(len(intervals)):
            if intervals[i][1] >= newInterval[0] and startMerge == -1:
                startMerge = i
            if intervals[i][0] <= newInterval[1]:
                endMerge = i

        # Edge cases for startMerge and endMerge
        if startMerge == -1:
            intervals.append(newInterval)
            return intervals 
        if endMerge == -1:
            intervals.insert(0, newInterval)
            return intervals
        
        # Merge the intervals
        merged = [min(intervals[startMerge][0], newInterval[0]), max(intervals[endMerge][1], newInterval[1])]
        
        # Remove the intervals that are merged
        intervals[startMerge:endMerge+1] = [merged]

        return intervals
                
