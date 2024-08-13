class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)  # Create a DP array of size target + 1
        dp[0] = 1  # Base case: one way to reach 0 (using no numbers)
        
        # Iterate through all sums from 1 to target
        for i in range(1, target + 1):
            for num in nums:  # For each number in nums
                if i >= num:  # Only consider the number if it does not exceed the current sum
                    dp[i] += dp[i - num]  # Add the ways to form the current sum
        
        return dp[target]  # Return the number of ways to form the target

