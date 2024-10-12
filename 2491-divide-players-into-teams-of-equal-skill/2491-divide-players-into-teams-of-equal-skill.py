class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n = len(skill)
        total_skill = sum(skill)

        # Calculate target skill for each team
        target_team_skill = total_skill // (n // 2)

        # If total skill cannot be evenly divided among teams
        if total_skill % (n // 2) != 0:
            return -1
        
        # Count frequency of each skill
        freq = Counter(skill)
        chemistry_sum = 0
        
        # Sort unique skills for pairing
        unique_skills = sorted(freq.keys())
        
        for s in unique_skills:
            while freq[s] > 0:
                complement = target_team_skill - s
                
                # Check if we can find a complementing skill
                if complement not in freq or freq[complement] <= 0:
                    return -1
                
                # Handle the case where both players have the same skill
                if s == complement:
                    if freq[s] < 2:
                        return -1
                    pairs = freq[s] // 2
                    chemistry_sum += pairs * (s * s)
                    freq[s] -= pairs * 2
                else:
                    pairs = min(freq[s], freq[complement])
                    chemistry_sum += pairs * (s * complement)
                    freq[s] -= pairs
                    freq[complement] -= pairs
        
        return chemistry_sum
