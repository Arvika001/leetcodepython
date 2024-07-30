class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)

        # Count total 'a's in the string
        counta = 0
        for i in range(n - 1, -1, -1):
            if s[i] == 'a':
                counta += 1

        # Initialize variables to track minimum deletions
        count = float('inf')  # To track the minimum deletions
        countb = 0  # To count the number of 'b's seen so far

        # Iterate through the string to calculate minimum deletions
        for i in range(n):
            if s[i] == 'a':
                counta -= 1  # One less 'a' to consider
            count = min(count, countb + counta)  # Update minimum deletions

            if s[i] == 'b':
                countb += 1  # Increment count of 'b's

        return count
        