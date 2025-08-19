from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        
        # Sort intervals by start value
        intervals.sort(key=lambda x: x[0])
        
        result = [intervals[0]]
        
        for interval in intervals[1:]:
            # If current interval overlaps with last merged interval
            if interval[0] <= result[-1][1]:
                # Merge them by updating the end of the last interval
                result[-1][1] = max(result[-1][1], interval[1])
            else:
                # No overlap, add current interval to result
                result.append(interval)
        
        return result