from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        start = nums[0]
        res = []
        for i in range(1, len(nums)):
            curr = nums[i]
            prev = nums[i-1]
            if curr != prev + 1:
                if prev == start:
                    res.append(str(start))
                else:
                    res.append(f"{start}->{prev}")
                start = curr
        # Add the last range
        if nums[-1] == start:
            res.append(str(start))
        else:
            res.append(f"{start}->{nums[-1]}")
        return res