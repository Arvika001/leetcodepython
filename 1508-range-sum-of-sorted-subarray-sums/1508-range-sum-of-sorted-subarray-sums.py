class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        MOD = 10**9 + 7  # Define the modulo constant
        subarray_sums = []  # List to store all subarray sums

        # Calculate all subarray sums
        for i in range(n):
            current_sum = 0
            for j in range(i, n):
                current_sum += nums[j]
                subarray_sums.append(current_sum)  # Add the current subarray sum

        # Sort the subarray sums in non-decreasing order
        subarray_sums.sort()

        # Calculate the sum of the numbers from index left to index right
        result = 0
        for i in range(left - 1, right):  # Convert to 0-based index
            result = (result + subarray_sums[i]) % MOD  # Use modulo to avoid overflow

        return result  # Return the final result
