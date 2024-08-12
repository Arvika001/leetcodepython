class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.K = k
        self.pq = []  # Initialize an empty min-heap

        # Add initial numbers to the min-heap
        for num in nums:
            heapq.heappush(self.pq, num)  # Add number to the heap
            if len(self.pq) > self.K:  # If the heap size exceeds k
                heapq.heappop(self.pq)  # Remove the smallest element

    def add(self, val: int) -> int:
        heapq.heappush(self.pq, val)  # Add the new value to the heap
        if len(self.pq) > self.K:  # If the heap size exceeds k
            heapq.heappop(self.pq)  # Remove the smallest element
        return self.pq[0]  # The root of the min-heap is the kth largest element
