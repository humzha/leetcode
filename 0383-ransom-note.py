from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """
        Determine if ransomNote can be constructed from the letters
        in magazine. Each letter in magazine can only be used once.

        Args:
            ransomNote (str): The note to construct.
            magazine (str): The source of letters.

        Returns:
            bool: True if ransomNote can be constructed from magazine,
            False otherwise.
        """
        magazine = Counter(magazine)
        ransom_note = Counter(ransomNote)
        for c, freq in ransom_note.items():
            if c not in magazine or freq > magazine[c]:
                return False
        return True
