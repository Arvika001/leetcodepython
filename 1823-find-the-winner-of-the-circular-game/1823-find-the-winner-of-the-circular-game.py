class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        friends = list(range(1, n + 1))
        current_position = 0
        
        while len(friends) > 1:
            to_remove = (current_position + k-1) % len(friends)
            friends.pop(to_remove)
            current_position = to_remove % len(friends)
            
        return friends[0]
       
		 
		
		
	    
        