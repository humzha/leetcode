from typing import List, Optional


def c_to_idx(c: str) -> int:
    return ord(c) - ord("a")


class TrieNode:
    def __init__(self):
        self.children: List[Optional[TrieNode]] = [None] * 26
        self.is_word = False

    def get_child(self, c: str) -> "TrieNode":
        # If the child doesn't exist create it
        if not self.children[c_to_idx(c)]:
            self.children[c_to_idx(c)] = TrieNode()
        return self.children[c_to_idx(c)]


class Trie:
    def __init__(self):
        """
        Initialize the Trie (prefix tree) with an empty root node.
        """
        self.root: TrieNode = TrieNode()
        # A word can be defined by the path to the trienode,
        # "a" -> 0
        # "ab" -> 0, 1

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.

        Args:
            word (str): The word to insert.

        Returns:
            None
        """
        curr = self.root
        for c in word:
            curr = curr.get_child(c)
        curr.is_word = True

    def search(self, word: str) -> bool:
        """
        Returns True if the word is in the trie.

        Args:
            word (str): The word to search for.

        Returns:
            bool: True if word exists, False otherwise.
        """
        curr = self.root
        for c in word:
            curr = curr.get_child(c)
        return curr.is_word

    def startsWith(self, prefix: str) -> bool:
        """
        Returns True if there is any word in the trie that starts
        with the given prefix.

        Args:
            prefix (str): The prefix to check.

        Returns:
            bool: True if any word starts with prefix, False otherwise.
        """
        curr = self.root
        for c in prefix:
            if not curr.children[c_to_idx(c)]:
                return False
            curr = curr.children[c_to_idx(c)]

        def dfs(curr: Optional[TrieNode]) -> bool:
            if not curr:
                return False
            elif curr.is_word:
                return True
            for child in curr.children:
                if dfs(child):
                    return True
            return False

        return dfs(curr)
