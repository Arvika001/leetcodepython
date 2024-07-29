class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # Create a graph using adjacency list representation
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        def dijkstra(source):
            # Min-heap priority queue
            min_heap = [(0, source)]  # (distance, city)
            distances = {i: float('inf') for i in range(n)}
            distances[source] = 0
            
            while min_heap:
                current_distance, current_city = heapq.heappop(min_heap)

                # If the distance is greater than the threshold, skip processing
                if current_distance > distanceThreshold:
                    continue

                for neighbor, weight in graph[current_city]:
                    distance = current_distance + weight

                    # Only consider this new path if it's better
                    if distance < distances[neighbor]:
                        distances[neighbor] = distance
                        heapq.heappush(min_heap, (distance, neighbor))

            # Count reachable cities within the distance threshold
            reachable_cities = sum(1 for dist in distances.values() if dist <= distanceThreshold)
            return reachable_cities

        min_reachable = float('inf')
        city_with_min_reachable = -1

        # Check each city as a potential starting point
        for city in range(n):
            reachable_count = dijkstra(city)

            # Update the result based on the criteria
            if reachable_count < min_reachable or (reachable_count == min_reachable and city > city_with_min_reachable):
                min_reachable = reachable_count
                city_with_min_reachable = city

        return city_with_min_reachable
