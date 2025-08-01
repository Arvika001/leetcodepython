class Solution {
public:
    int longestOnes(vector<int>& nums, int k) {
        int l = 0, cnt = 0;
        for (int x : nums) {
            cnt += x ^ 1;
            if (cnt > k) {
                cnt -= nums[l++] ^ 1;
            }
        }
        return nums.size() - l;
    }
};
