from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water = 0
        left, right = 0, len(height)-1

        while left<right:
            rightHeight, leftHeight = height[right], height[left]
            water = min(rightHeight, leftHeight) * (right-left)
            print(f"{leftHeight}:{rightHeight}:{right-left}")
            max_water = max(water, max_water)

            if rightHeight < leftHeight:
                right -= 1
            else:
                left += 1
        
        return max_water