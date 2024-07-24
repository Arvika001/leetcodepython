class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        # Helper function to get the mapped number
        def getMappedNum(num: int) -> int:
            if num < 10:
                return mapping[num]

            mappedNum = 0
            placeValue = 1

            while num > 0:
                lastDigit = num % 10
                mappedDigit = mapping[lastDigit]
                mappedNum += mappedDigit * placeValue

                placeValue *= 10
                num //= 10

            return mappedNum

        # Create a list of tuples (mapped value, original index)
        mapped_nums = [(getMappedNum(num), i) for i, num in enumerate(nums)]
        
        # Sort based on the mapped values, maintaining original order for ties
        mapped_nums.sort(key=lambda x: (x[0], x[1]))

        # Extract the sorted original numbers based on their mapped values
        return [nums[i] for _, i in mapped_nums]
    