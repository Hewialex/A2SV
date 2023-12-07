from typing import List

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        concat_word1 = "".join(word1)
        concat_word2 = "".join(word2)
        
        if concat_word1 == concat_word2:
          return True
        else:
          return False
