from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = {}
        max = None
        max_count = 0
        for num in nums:
            if num not in counts.keys():
                counts[num] = 0
            counts[num] += 1
            count = counts[num]
            if count > max_count:
                max_count = count
                max = num

        return max