from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l,r = 0,0
        sum = 0
        res  = None

        for r in range(0, len(nums)):
            sum += nums[r]

            while sum >= target:
                res = r-l + 1 if not res else min(res, r-l + 1)
                sum -= nums[l]
                l+=1
        return res if res else 0