/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<TreeNode*> delNodes(TreeNode* root, vector<int>& to_delete) {
        unordered_set<int> to_delete_set(to_delete.begin(), to_delete.end());
        vector<TreeNode*> result;
        dfs(root, true, to_delete_set, result);
        return result;
    }

private:
    TreeNode* dfs(TreeNode* node, bool is_root, unordered_set<int>& to_delete_set, vector<TreeNode*>& result) {
        if (!node) {
            return nullptr;
        }

        bool is_deleted = to_delete_set.count(node->val);
        if (is_root && !is_deleted) {
            result.push_back(node);
        }

        node->left = dfs(node->left, is_deleted, to_delete_set, result);
        node->right = dfs(node->right, is_deleted, to_delete_set, result);

        return is_deleted ? nullptr : node;
    }
};