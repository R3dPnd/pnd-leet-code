

from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        nums1_copy = nums1[:m]

        a,b = 0,0
        for i in range(n + m):
            if b >= n or (a < m and nums1_copy[a] <= nums2[b]):
                print(b)
                nums1[i] = nums1_copy[a]
                a += 1
            else:
                nums1[i] = nums2[b]
                b += 1