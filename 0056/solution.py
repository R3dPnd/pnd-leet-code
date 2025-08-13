from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        intervals = sorted(intervals, key=lambda x: x[0])
        i = 1
        solution = []
        while i<n:
            curr = intervals[i]
            prev = intervals[i-1]
            if prev[1] >= curr[0]:
                n-=1
                curr[0] = min(curr[0], prev[0])
                curr[1] = max (prev[1],curr[1])
                print(intervals)
            else:
                i+=1
                solution.append(prev)

        return solution