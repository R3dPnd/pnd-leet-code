from typing import List

# Why This Works:
# 
# Greedy Choice: 
# At each step, we always choose to jump when we reach the boundary of our current range, ensuring we don't take unnecessary jumps.
# 
# Optimal Substructure: 
# The minimum jumps to reach position i plus the minimum jumps from position i to the end equals the minimum jumps to reach the end.
# 
# Range Expansion: 
# By updating current_end to farthest, we're always expanding our reachable range as much as possible with each jump.

class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <1:
            return 0
        jumps = 0
        current_end = 0
        farthest = 0

        for i in range(len(nums)-1):
            farthest = max(farthest, i + nums[i])
            
            if i == current_end:
                jumps += 1
                current_end = farthest
        return jumps