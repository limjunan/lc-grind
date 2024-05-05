from typing import List
# Submitted Solution 1
# Did not take into consideration that an interval can be complely inside another interval

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals

        intervals.sort(key=lambda x: x[0])
        print(intervals)
        outputInterval = []

        startMerge = -1
        startInt = 0
        endMerge = -1
        endInt = 0

        for i in range(1, len(intervals)):
            if intervals[i][0] > intervals[i-1][1]:
                if startMerge == -1:
                    outputInterval.append(intervals[i - 1])
                    
                else:
                    merged = [startInt, endInt]
                    outputInterval.append(merged)
                    startMerge = -1

                if i == len(intervals) - 1:
                        outputInterval.append(intervals[i])

                continue
            
            if startMerge == -1:
                startMerge = i - 1
                endMerge = startMerge
                startInt = intervals[i - 1][0]
                endInt = max(intervals[i][1], intervals[i - 1][1])

            endMerge += 1
            startInt = min(startInt, intervals[i][0])
            endInt = max(endInt, intervals[i][1])

            if i == len(intervals) - 1:
                merged = [startInt, endInt]
                outputInterval.append(merged)
        
        return outputInterval
            

# Submitted Solution 2
# SUPER SLOW LOL

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals

        intervals.sort(key=lambda x: x[0])
        print(intervals)
        outputInterval = []
        merged = []

        for i in range(len(intervals) - 1):
            if merged:
                if intervals[i + 1][0] <= merged[1]:
                    merged = [min(merged[0], intervals[i + 1][0]), max(merged[1], intervals[i + 1][1])]
                else:
                    outputInterval.append(merged)
                    merged = []
            else:
                if intervals[i + 1][0] <= intervals[i][1]:
                    merged = [min(intervals[i][0], intervals[i + 1][0]), max(intervals[i][1], intervals[i + 1][1])]
                else:
                    outputInterval.append(intervals[i])

            if i == len(intervals) - 2 and merged:
                outputInterval.append(merged)
            elif i == len(intervals) - 2 and not merged:
                outputInterval.append(intervals[i + 1])

        return outputInterval

        
            
