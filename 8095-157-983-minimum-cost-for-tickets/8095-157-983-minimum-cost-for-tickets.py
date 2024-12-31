class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        @cache
        def dfs(i: int) -> int:
            if i >= n:
                return 0
            
            ans = float('inf')
            for c, v in zip(costs, valid):
                # Find the index of the first day that is not covered by this ticket
                j = bisect_left(days, days[i] + v)
                ans = min(ans, c + dfs(j))
            return ans

        n = len(days)
        valid = [1, 7, 30]  # Valid ticket durations
        return dfs(0)
