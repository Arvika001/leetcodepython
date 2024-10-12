class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len_s1 = len(s1)
        len_s2 = len(s2)

        # If s1 is longer than s2, it's impossible to find a permutation
        if len_s1 > len_s2:
            return False
        
        # Create frequency arrays for s1 and the first window of s2
        count_s1 = [0] * 26  # For 'a' to 'z'
        window_count = [0] * 26
        
        # Fill frequency array for s1
        for char in s1:
            count_s1[ord(char) - ord('a')] += 1
        
        # Fill frequency array for the first window in s2
        for char in s2[:len_s1]:
            window_count[ord(char) - ord('a')] += 1
        
        # Function to compare two frequency arrays
        def matches(count_a, count_b):
            return all(a == b for a, b in zip(count_a, count_b))
        
        # Check if the first window matches
        if matches(count_s1, window_count):
            return True
        
        # Slide the window over s2
        for i in range(len_s1, len_s2):
            # Add the new character to the window
            window_count[ord(s2[i]) - ord('a')] += 1
            
            # Remove the oldest character from the window
            window_count[ord(s2[i - len_s1]) - ord('a')] -= 1
            
            # Compare frequency arrays
            if matches(count_s1, window_count):
                return True
        
        return False
