class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        
        for detail in details:
            # Extract the age from the string (characters at indices 11 and 12)
            age_str = detail[11:13]  # The age is represented by the 12th and 13th characters
            age = int(age_str)  # Convert the age string to an integer
            
            # Check if the age is greater than 60
            if age > 60:
                count += 1
                
        return count
