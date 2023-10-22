'''
Given an array of meeting time intervals where intervals[i] = [starti, endi], determine if a person could attend all meetings.

'''

# My solution #
class Solution:
    def canAttendMeetings(self, intervals):

        # Check if any of the start times are before the end times
        meetings = len(intervals)
        for i in range(meetings):

            meetingStart = intervals[i][0]
            meetingEnd = intervals[i][1]

            for j in range(meetings):

                if (i == j):
                    continue

                nextMeetingStart = intervals[j][0]
                nextMeetingEnd = intervals[j][1]

                # If the start and end times aren't both before or after the start or  end times
                # So if the 

                if (not ((meetingStart < nextMeetingStart and meetingEnd <= nextMeetingStart) or (meetingStart >= nextMeetingEnd and meetingEnd > nextMeetingEnd))):
                    return False
        return True


# Approach 1: Brute Force
from typing import List
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        def overlap(interval1: List[int], interval2: List[int]) -> bool:
            return (interval1[0] >= interval2[0] and interval1[0] < interval2[1]
                or interval2[0] >= interval1[0] and interval2[0] < interval1[1])

        for i in range(len(intervals)):
            for j in range(i + 1, len(intervals)):
                if overlap(intervals[i], intervals[j]):
                    return False
        return True
# Time complexity: O(n^2) because of the duoble loop
# Space complexity: O(1) because no additional space is used


# Approach 2: Sorting #
# from typing import List
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort() # Sort meetings by start time
        for i in range(len(intervals) - 1):
            if intervals[i][1] > intervals[i + 1][0]: # Check that each meeting ends before the next one begins
                return False
        return True
# Time complexity: O(nlog(n)) because of the sorting required, only O(n) time is required to determine if there is overlap
# Space complexity: O(1) because no additional space is allocated


# Unit Tests
import unittest
class TestSolution(unittest.TestCase):
    def test1(self):
        intervals = [[0,30],[5,10],[15,20]]
        obj = Solution
        self.assertFalse(Solution.canAttendMeetings(obj, intervals))
        
    def test2(self):
        intervals = [[7,10],[2,4]]
        obj = Solution
        self.assertTrue(Solution.canAttendMeetings(obj, intervals))

if __name__ == '__main__':
    unittest.main()