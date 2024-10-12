from typing import List

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total_sum = sum(nums)
        remainder = total_sum % p
        
        # If total_sum is already divisible by p, no need to remove anything
        if remainder == 0:
            return 0
        
        # If total_sum < p, it's impossible to make it divisible by p
        if total_sum < p:
            return -1
        
        # Dictionary to store the most recent index of each mod value
        mod_indices = {0: -1}  # Initialize with mod 0 at index -1
        current_sum = 0
        min_length = float('inf')  # Initialize to infinity
        
        for i in range(len(nums)):
            current_sum += nums[i]
            current_mod = current_sum % p
            
            # Calculate target mod value which would balance out current_mod
            target_mod = (current_mod - remainder + p) % p
            
            # Check if this target mod has been seen before
            if target_mod in mod_indices:
                min_length = min(min_length, i - mod_indices[target_mod])
            
            # Store the most recent index for this current_mod
            mod_indices[current_mod] = i
            
        # Check if we found a valid subarray length
        return min_length if min_length < len(nums) else -1