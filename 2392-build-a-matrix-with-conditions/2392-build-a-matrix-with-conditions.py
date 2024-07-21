class Solution:
    def topoSort(self, edges: List[List[int]], n: int) -> List[int]:
        # Create an adjacency list for the directed graph
        adj = defaultdict(list)
        in_degree = [0] * (n + 1)  # In-degree of each node

        # Build the graph
        for u, v in edges:
            adj[u].append(v)
            in_degree[v] += 1
        
        # Queue for nodes with no incoming edges (in-degree 0)
        queue = deque()
        for i in range(1, n + 1):
            if in_degree[i] == 0:
                queue.append(i)

        order = []
        while queue:
            node = queue.popleft()
            order.append(node)

            # Decrease the in-degree of neighbor nodes
            for neighbor in adj[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        return order

    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        # Get the topological order for rows and columns
        orderRows = self.topoSort(rowConditions, k)
        orderColumns = self.topoSort(colConditions, k)

        # Check if topological sort is possible
        if len(orderRows) != k or len(orderColumns) != k:
            return []

        # Create the k x k matrix
        matrix = [[0] * k for _ in range(k)]
        for i in range(k):
            for j in range(k):
                if orderRows[i] == orderColumns[j]:
                    matrix[i][j] = orderRows[i]

        return matrix

     