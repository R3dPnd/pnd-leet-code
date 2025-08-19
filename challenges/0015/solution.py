from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Alternative approach using hash set
        Time Complexity: O(n²)
        Space Complexity: O(n)
        """
        if len(nums) < 3:
            return []
        
        solutions = []
        seen = set()
        
        for i in range(len(nums)):
            # Use two-sum approach for the remaining elements
            target = -nums[i]
            two_sum_set = set()
            
            for j in range(i + 1, len(nums)):
                complement = target - nums[j]
                
                if complement in two_sum_set:
                    # Create sorted triplet to avoid duplicates
                    triplet = sorted([nums[i], nums[j], complement])
                    triplet_tuple = tuple(triplet)
                    
                    if triplet_tuple not in seen:
                        seen.add(triplet_tuple)
                        solutions.append(triplet)
                        
                two_sum_set.add(nums[j])
        
        return solutions