from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        results =  []
        size = len(intervals)
        i = 0

        # Case 1: No overlapping before merging intervals
        while i< size and intervals[i][1] < newInterval[0]:
            results.append(intervals[i])
            i +=1

        # Case 2: Overlapping and merging intervals
        while i<size and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        results.append(newInterval)

        # Case 3: No overlapping after merging new Interval
        while i<size:
            results.append(intervals[i])
            i += 1

        return results