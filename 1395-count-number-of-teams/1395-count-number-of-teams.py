class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        teams = 0

        # Iterate through each soldier as the middle member of the team
        for j in range(n):
            countSmallerLeft = 0
            countLargerLeft = 0
            countSmallerRight = 0
            countLargerRight = 0

            # Count how many ratings are smaller and larger to the left of j
            for i in range(j):
                if rating[i] < rating[j]:
                    countSmallerLeft += 1
                elif rating[i] > rating[j]:
                    countLargerLeft += 1

            # Count how many ratings are smaller and larger to the right of j
            for k in range(j + 1, n):
                if rating[j] < rating[k]:
                    countLargerRight += 1
                elif rating[j] > rating[k]:
                    countSmallerRight += 1

            # Calculate the number of valid teams with j as the middle member
            teams += countLargerLeft * countSmallerRight  # Increasing team
            teams += countSmallerLeft * countLargerRight  # Decreasing team

        return teams
