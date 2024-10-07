class Solution:
    def minLength(self, s: str) -> int:
        stack = []
        for c in s:
            # Check if we can remove "AB" or "CD"
            if stack and ((c == 'B' and stack[-1] == 'A') or (c == 'D' and stack[-1] == 'C')):
                stack.pop()  # Remove the last character if it forms "AB" or "CD"
            else:
                stack.append(c)  # Otherwise, add the current character to the stack
        return len(stack)  # The length of the remaining characters in the stack
