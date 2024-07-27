class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        INF = float('inf')
        # Initialize the distances matrix
        distances = [[INF] * 26 for _ in range(26)]

        # Fill in the direct transformation costs
        for o, c, co in zip(original, changed, cost):
            s = ord(o) - ord('a')
            t = ord(c) - ord('a')
            distances[s][t] = min(distances[s][t], co)

        # Floyd-Warshall algorithm to find minimum costs between all pairs
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    distances[i][j] = min(distances[i][j], distances[i][k] + distances[k][j])

        totalCost = 0

        # Calculate the total cost to convert source to target
        for i in range(len(source)):
            if source[i] == target[i]:
                continue  # No cost if characters are the same

            srcIndex = ord(source[i]) - ord('a')
            tgtIndex = ord(target[i]) - ord('a')

            if distances[srcIndex][tgtIndex] == INF:
                return -1  # Impossible to convert this character
            else:
                totalCost += distances[srcIndex][tgtIndex]

        return totalCost
        