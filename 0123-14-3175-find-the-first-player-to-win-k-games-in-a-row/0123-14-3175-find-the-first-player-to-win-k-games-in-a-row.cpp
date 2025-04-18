class Solution {
public:
    int findWinningPlayer(vector<int>& skills, int k) {
        int n = skills.size();
        k = min(k, n - 1);
        int i = 0, cnt = 0;
        for (int j = 1; j < n; ++j) {
            if (skills[i] < skills[j]) {
                i = j;
                cnt = 1;
            } else {
                ++cnt;
            }
            if (cnt == k) {
                break;
            }
        }
        return i;
    }
};
