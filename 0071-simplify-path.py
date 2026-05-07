class Solution:
    """Solution for simplifying an absolute Unix-style file path.

    Given a string path representing an absolute Unix path, return the
    simplified canonical path. A canonical path has no trailing '/', no
    consecutive '/', and resolves '.' and '..' directory references.
    """

    def simplifyPath(self, path: str) -> str:
        # Your implementation here
        tokens = path.split('/')
        path = []
        for t in tokens:
            # '// ///'
            if t == '' or t == '.':
                continue
            if t == '..':
                # Path is guaranteed to be valid
                path.pop()
            # '..., ....' are treated as dir names
            else:
                path.append(t)
        return '/' + '/'.join(path)