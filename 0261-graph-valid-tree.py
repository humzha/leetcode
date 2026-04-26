from collections import defaultdict

class Solution:
    """Solution for determining whether a given graph is a valid tree.

    You are given `n` nodes labeled from 0 to n - 1 and a list of undirected
    edges. Return True if the edges form a valid tree, otherwise False.

    A valid tree must be connected and contain no cycles.
    """

    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        """Checks if the given graph forms a valid tree.

        Args:
            n (int): Number of nodes labeled from 0 to n - 1.
            edges (list[list[int]]): List of undirected edges.

        Returns:
            bool: True if the graph is a valid tree, otherwise False.
        """
        # Convert edges to adj_list
        adj_list = defaultdict(set)
        for a, b in edges:
            adj_list[a].add(b)
            adj_list[b].add(a)

        # DFS
        # start at node 0
        visited = [False for _ in range(n)]
        def detect_cycle(node: int, parent_node) -> bool:
            # DFS cycle detection
            if visited[node]:
                return True
            visited[node] = True

            for nei in adj_list[node]:
                if nei == parent_node:
                    continue
                if detect_cycle(nei, node):
                    return True
            return False

        cyclic = detect_cycle(0, -1)
        return all(visited) and not cyclic