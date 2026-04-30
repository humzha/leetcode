class Solution:
    """Solution for counting connected components in an undirected graph.

    Given `n` nodes labeled from 0 to n - 1 and a list of undirected edges,
    return the number of connected components in the graph.
    """

    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        """Counts the number of connected components.

        Args:
            n (int): Number of nodes.
            edges (list[list[int]]): Undirected edges between nodes.

        Returns:
            int: Number of connected components.
        """
        rank = [1 for _ in range(n)]
        parent = [i for i in range(n)]

        def find(x: int) -> int:
            if parent[x] == x:
                return x
            parent[x] = find(parent[x])
            return parent[x]
            
        def union(a: int, b: int) -> bool:
            parent_a, parent_b = find(a), find(b)
            if parent_a == parent_b:
                return False
            if rank[parent_a] == rank[parent_b]:
                rank[parent_a] += 1
                parent[parent_b] = parent_a
            elif rank[parent_a] > rank[parent_b]:
                parent[parent_b] = parent_a
            else:
                parent[parent_a] = parent_b
            return True

        for a, b in edges:
            union(a, b)
            
        return sum([1 if find(x) == x else 0 for x in range(n)])
            