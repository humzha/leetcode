class Solution:
    """Solution for finding all roots of minimum height trees in an undirected tree.

    Given a tree of `n` nodes labeled from `0` to `n - 1` and a list of `n - 1`
    undirected edges, return all nodes that, when chosen as tree roots, result in
    the minimum possible tree height. The height of a rooted tree is defined as
    the number of edges on the longest downward path between the root and a leaf.
    You may return the answer in any order.:contentReference[oaicite:0]{index=0}
    """

    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        """Finds all minimum height tree root labels.

        Args:
            n (int): Number of nodes in the tree.
            edges (List[List[int]]): List of `n - 1` undirected edges connecting nodes.

        Returns:
            List[int]: A list of all root labels that produce a minimum height tree.
        """
        if not edges and n == 1:
            return [0]

        # Build adjacency list
        adj_list: list[set[int]] = [set() for _ in range(n)]
        connected_nodes = set()
        for a, b in edges:
            adj_list[a].add(b)
            adj_list[b].add(a)
            connected_nodes.add(a)
            connected_nodes.add(b)
            
        # Peel leaf nodes, topologial sort
        while len(connected_nodes) > 2:
            # Could optimize to not be O(n**2) by tracking how many edges each node has in a map
            leaf_nodes = []
            for node_idx in connected_nodes:
                if len(adj_list[node_idx]) == 1:
                    leaf_nodes.append(node_idx)
                    
            for node_idx in leaf_nodes:
                nei_idx = adj_list[node_idx].pop()
                adj_list[nei_idx].remove(node_idx)
                
                if not adj_list[node_idx]:
                    connected_nodes.remove(node_idx)
                
        return list(connected_nodes)