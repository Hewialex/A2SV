class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        arr = []
        s = set("qwertyuiop")
        r = set("asdfghjkl")
        t = set("zxcvbnm")
        
        for word in words:
            word_set = set(word.lower())
            if word_set.issubset(s) or word_set.issubset(r) or word_set.issubset(t):
                arr.append(word)
                
        return arr