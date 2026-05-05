from collections import deque

class Solution:
    """Solution for finding the length of the shortest word transformation sequence.

    Given two words beginWord and endWord, and a dictionary wordList,
    return the number of words in the shortest transformation sequence
    from beginWord to endWord, or 0 if no such sequence exists.
    """

    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        word_list = set(wordList)
        word_list.add(beginWord)
        if endWord not in word_list:
            return 0
        
        q = deque([(beginWord, 1)])
        visited = set([beginWord])
        while q:
            word, dist = q.popleft()
            if word == endWord:
                return dist

            one_edit_word = list(word)
            for i in range(len(word)):
                for j in range(26):
                    edit_c = chr(ord('a') + j)
                    if edit_c == word[i]:
                        continue
                    one_edit_word[i] = edit_c
                    nei = ''.join(one_edit_word)
                    if nei in word_list and nei not in visited:
                        q.append((nei, dist + 1))
                        visited.add(nei)
                one_edit_word[i] = word[i]
        return 0

        # word_list = set(wordList)
        # word_list.add(beginWord)
        # if endWord not in word_list:
        #     return 0
        
        # def one_edit_off(a: str, b: str) -> bool:
        #     # at most one edit
        #     edited = False
        #     for i in range(len(a)):
        #         if a[i] != b[i]:
        #             if edited:
        #                 return False
        #             edited = True
        #     return True
        # adj_list = {}
        # for a in word_list:
        #     for b in word_list:
        #         if a == b:
        #             continue
        #         if one_edit_off(a, b):
        #             adj_list[a].add(b)
        #             adj_list[b].add(a)
