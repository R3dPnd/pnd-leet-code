class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        start = nums[0]
        res = []
        for i in range(1, len(nums)):
            curr = nums[i]
            prev = nums[i-1]
            if curr != prev + 1 or i == len(nums)-1:
                if prev == start:
                    res.append(str(start))
                else: 
                    res.append(str(start) + "->" + str(prev))
                start = curr
        return res