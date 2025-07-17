from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        count = 1
        while i < len(nums):
            if nums[i] == nums[i-1]:
                count += 1
                print(nums[i])
                if count > 2:
                    nums.pop(i)
                    count -= 1
                    i -= 1
            else:
                count = 1
                
            i += 1
        return len(nums)