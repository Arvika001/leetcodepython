class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        A = len(customers)
        
        total_waiting_time = 0
        current_time = 0
        
        for arrival, preparation in customers:
            current_time = max(current_time, arrival)
            current_time += preparation
            
            total_waiting_time += current_time - arrival
        
        return total_waiting_time / A
        