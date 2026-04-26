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

        parent = {i: i for i in range(n)}
        rank = {i: 1 for i in range(n)}

        def find(x: int) -> int:
            if parent[x] == x:
                return x
            parent[x] = find(parent[x])
            return parent[x]
        
        def union(a: int, b: int) -> bool: 
            """
            Return false if the two are already in the same set
            True otherwise
            """
            parent_a = find(a)
            parent_b = find(b)
            if parent_a == parent_b:
                return False

            if rank[parent_a] > rank[parent_b]:
                parent[parent_b] = parent_a
            elif rank[parent_a] < rank[parent_b]:
                parent[parent_a] = parent_b
            else:
                parent[parent_a] = parent_b
                rank[parent_b] += 1
                

            return True

        for a, b in edges:
            if not union(a, b):
                return False
                
        return all([find(x) == find(0) for x in range(n)])
        