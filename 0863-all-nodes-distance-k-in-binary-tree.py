from collections import defaultdict, deque

class Solution:
    """Solution for finding all nodes at distance k from a target node.

    Given the root of a binary tree, a target node, and an integer k,
    return all node values that are exactly k edges away from the target.
    """

    def distanceK(self, root: 'TreeNode', target: 'TreeNode', k: int) -> list[int]:
        # Your implementation here
        # all the values in node.val are unique
        adj_list = defaultdict(list)
        def dfs(root: 'TreeNode'):
            if not root:
                return None

            if root.left:
                adj_list[root.left.val].append(root.val)
                adj_list[root.val].append(root.left.val)
            if root.right:
                adj_list[root.right.val].append(root.val)
                adj_list[root.val].append(root.right.val)
            dfs(root.left)
            dfs(root.right)
        dfs(root)

        queue = deque([(target.val, 0)])
        visited = set([target.val])
        res = []
        while queue:
            n, dist = queue.popleft()
            if dist > k:
                break
            elif dist == k:
                res.append(n)
            for nei in adj_list[n]:
                if nei not in visited:
                    queue.append((nei, dist + 1))
                    visited.add(nei)
            
        return res