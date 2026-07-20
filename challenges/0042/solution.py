from typing import List


class Solution:
    def trap_brute_force(self, height: List[int]) -> int:
        res = 0

        for i in range(1, len(height)-1):
            left_max, right_max = 0, 0

            #search for the left max
            for j in range(i, -1, -1):
                left_max = max(left_max, height[j])
            #search for the right max
            for j in range(i, len(height)):
                right_max = max(right_max, height[j])
            res += min(left_max, right_max) - height[i]

        return res
    
    def trap(self, height: List[int]) -> int:
        # Find the maximum height from the left and right for each position
        if not height:
            return 0
        res = 0 
        size = len (height)


        left_max, right_max = [0] * size, [0] * size

        # Find all of the maxes from the left
        for i in range(1, size):
            left_max[i] = max(left_max[i-1], height[i-1])

        # Find all of the maxes from the right
        for i in range(size-2, -1, -1):
            right_max[i] = max(right_max[i+1], height[i+1])

        # Calculate the trapped water for each position
        for i in range(size):
            water_level = min(left_max[i], right_max[i])
            if water_level > height[i]:
                res += water_level - height[i]

        return res
