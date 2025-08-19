from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashset = {}

        for i in range(len(numbers)):
            diff = target - numbers[i]
            if diff in hashset.keys():
                print(hashset)
                return [hashset[diff]+1, i+1]
            hashset[numbers[i]] = i
        return []