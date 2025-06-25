from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
        
    def quickTwoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        hashMap = {}

        for i in range(n):
            hashMap[nums[i]] = i

        for i in range(n):
            complement = target - nums[i]
            if complement in hashMap and hashMap[complement] != i:
                return [i, hashMap[complement]]
        return []


