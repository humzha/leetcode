import heapq
from collections import Counter

class Solution:
    """Solution for returning the k most frequent words.

    Given a list of strings `words` and an integer `k`, return the `k` most
    frequent words. The result should be sorted by frequency in descending
    order. If multiple words have the same frequency, they should be sorted
    in lexicographical (alphabetical) order.
    """  

    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        """Finds the k most frequent words with specific ordering rules.

        Args:
            words (list[str]): List of lowercase words.
            k (int): Number of top frequent words to return.

        Returns:
            list[str]: The k most frequent words sorted by frequency descending,
                then lexicographically ascending.
        """
        word_to_freq = Counter(words)
        heap_fw = [(-freq, word) for word, freq in word_to_freq.items()]
        heapq.heapify(heap_fw)
        
        res = []
        for _ in range(k):
            res.append(heapq.heappop(heap_fw)[1])
        return res