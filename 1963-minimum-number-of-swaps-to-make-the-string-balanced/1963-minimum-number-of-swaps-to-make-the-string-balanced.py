class Solution:
    def minSwaps(self, s: str) -> int:
        # Initialize variables to track balance and swaps needed
        balance = 0
        unmatched_closing = 0
        
        for char in s:
            if char == '[':
                balance += 1  # Increase balance for an opening bracket
            else:
                balance -= 1  # Decrease balance for a closing bracket
            
            # If balance goes negative, we have more closing brackets
            if balance < 0:
                unmatched_closing += 1  # Count unmatched closing brackets
                balance = 0  # Reset balance after counting the swap needed
        
        # Each two unmatched closing brackets require one swap
        return (unmatched_closing + 1) // 2
