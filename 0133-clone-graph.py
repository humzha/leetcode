class Solution:
    def cloneGraph(self, node: "Optional[Node]") -> "Optional[Node]":
        """
        Given a reference to a node in a connected undirected graph,
        return a deep copy (clone) of the graph. Each node contains
        a value and a list of neighbors.

        Every value is unique

        Args:
            node (Optional[Node]): A node in the graph to clone.

        Returns:
            Optional[Node]: The cloned graph’s corresponding node.

        class Node {
            public int val;
            public List<Node> neighbors;
        }
        """
        val_to_node = {}

        def clone_graph(node: Optional[Node]) -> Optional[Node]:
            if not node:
                return None
            if node.val not in val_to_node:
                val_to_node[node.val] = Node()
                val_to_node[node.val].val = node.val
                for n in node.neighbors:
                    val_to_node[node.val].neighbors.append(clone_graph(n))
            return val_to_node[node.val]

        return clone_graph(node)
