from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n
        
        def reverse(start, end):
            nonlocal nums
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start, end = start + 1, end - 1
        
        reverse(0, n-1)
        reverse(0, k-1)
        reverse(k, n-1)


if __name__ == "__main__":
    solution = Solution()
    nums = [1,2,3,4,5,6,7]
    k = 3
    solution.rotate(nums, k)
    print(nums)
