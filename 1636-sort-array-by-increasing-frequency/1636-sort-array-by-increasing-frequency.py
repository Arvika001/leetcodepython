class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        # Count the frequency of each number
        freq = Counter(nums)
        
        # Sort the numbers based on frequency and then by value
        sorted_nums = sorted(nums, key=lambda x: (freq[x], -x))
        
        return sorted_nums  