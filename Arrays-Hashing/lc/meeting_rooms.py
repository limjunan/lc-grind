# Given an array of meeting time intervals consisting of start and end times
# [[s1,e1],[s2,e2],...] (si < ei),
# determine if a person could attend all meetings.

# https://www.lintcode.com/problem/920/

class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """
        # Sort the intervals by start time
        intervals.sort(key=lambda x: x[0])
        
        for i in range(1, len(intervals)):
            # If the start time of the current interval is less than the end time of the previous interval
            if intervals[i][0] < intervals[i-1][1]:
                return False
        return True