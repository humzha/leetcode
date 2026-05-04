# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    """Codec for serializing and deserializing a binary tree.

    Design an algorithm to serialize a binary tree to a string and
    deserialize that string back to the original tree structure.
    """

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string."""
        # Your implementation here
        res = []
        def preorder(root: TreeNode | None):
            if not root:
                res.append('None')
                return
            res.append(str(root.val))
            preorder(root.left)
            preorder(root.right)
        preorder(root)
        return '#'.join(res)

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree."""
        # Your implementation here
        token_iter = iter(data.split('#'))
        def deser(it) -> TreeNode | None:
            data = next(token_iter)
            if data == 'None':
                return None
            node = TreeNode(int(data))
            node.left = deser(token_iter)
            node.right = deser(token_iter)
            return node
        return deser(token_iter)