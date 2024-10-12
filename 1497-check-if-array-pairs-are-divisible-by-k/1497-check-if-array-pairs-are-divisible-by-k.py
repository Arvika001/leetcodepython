class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        # Create a frequency dictionary for remainders
        remainder_count = defaultdict(int)
        
        # Count the occurrences of each remainder
        for num in arr:
            remainder = num % k
            # Adjust negative remainders to be positive
            if remainder < 0:
                remainder += k
            remainder_count[remainder] += 1
        
        # Check pairing conditions
        for r in range(k):
            if r == 0:  # Special case for remainder 0
                if remainder_count[r] % 2 != 0:
                    return False
            elif r * 2 == k:  # Special case for k/2 when k is even
                if remainder_count[r] % 2 != 0:
                    return False
            else:
                if remainder_count[r] != remainder_count[k - r]:
                    return False
        
        return True
