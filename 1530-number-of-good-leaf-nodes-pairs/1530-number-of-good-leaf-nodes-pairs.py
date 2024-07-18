# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def makeGraph(self, root: TreeNode, prev: TreeNode, adj: dict, leaf_nodes: set):
        if not root:
            return

        if not root.left and not root.right:  # Leaf node
            leaf_nodes.add(root)

        if prev:
            adj.setdefault(root, []).append(prev)
            adj.setdefault(prev, []).append(root)

        self.makeGraph(root.left, root, adj, leaf_nodes)
        self.makeGraph(root.right, root, adj, leaf_nodes)

    def countPairs(self, root: TreeNode, distance: int) -> int:
        adj = {}  # Graph
        leaf_nodes = set()  # Leaf nodes

        self.makeGraph(root, None, adj, leaf_nodes)

        count = 0  # Count of good node pairs

        for leaf in leaf_nodes:
            # Perform BFS and see if you can find other leaf nodes within distance
            queue = [leaf]
            visited = set([leaf])

            for level in range(distance + 1):  # Only go till level <= distance
                size = len(queue)
                while size > 0:
                    curr = queue.pop(0)
                    size -= 1

                    if curr != leaf and curr in leaf_nodes:
                        count += 1

                    for neighbor in adj.get(curr, []):
                        if neighbor not in visited:
                            queue.append(neighbor)
                            visited.add(neighbor)

        return count // 2        