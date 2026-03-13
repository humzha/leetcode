class TrieNode:
    def __init__(self) -> None:
        self.children: list["TrieNode" | None] = [None] * 26
        # Denotes whether the path that terminates at this Trienode is a word
        self.is_word: bool = False

class WordDictionary:
    """Data structure that supports adding words and searching with wildcards.

    Design a data structure that allows adding words and searching for them
    later. The search query may contain the '.' wildcard character, which
    can match any single letter.
    """

    def __init__(self) -> None:
        """Initializes the WordDictionary object."""
        self.root = TrieNode()

    def _navigate_to_word(self, word: str, make_path: bool) -> TrieNode | None:
        """Navigate to the word from the node
        make_path: bool denotes if we will create nodes on the way to it

        Returns None if we can't navigate to it
        """
        curr_node: TrieNode = self.root
        for c in word:
            i = ord(c.lower()) - ord('a')
            if curr_node.children[i] is None:
                if make_path:
                    curr_node.children[i] = TrieNode()
                else:
                    return None
            curr_node = curr_node.children[i]
        return curr_node


    def addWord(self, word: str) -> None:
        """Adds a word to the data structure.

        Args:
            word (str): The word to add.
        """
        node = self._navigate_to_word(word, True)
        node.is_word = True


    def search(self, word: str) -> bool:
        """Searches for a word or wildcard pattern.

        The input word may contain '.' characters, which match any single
        letter.

        Args:
            word (str): The search query string.

        Returns:
            bool: True if any stored word matches the query; otherwise False.
        """
        def dfs(word: str, i: int, node: TrieNode) -> bool:
            if not node:
                return False
            if i == len(word):
                return node.is_word
            if word[i] == '.':
                for child_idx in range(26):
                    if dfs(word, i + 1, node.children[child_idx]):
                        return True
            elif dfs(word, i + 1, node.children[ord(word[i]) - ord('a')]):
                return True
            return False
        
        return dfs(word, 0, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
