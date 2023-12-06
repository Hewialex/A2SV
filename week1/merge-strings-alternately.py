class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""

        # Find the minimum length of the two words
        min_length = min(len(word1), len(word2))

        # Merge alternating letters from word1 and word2
        for i in range(min_length):
            result += word1[i] + word2[i]

        # Append the remaining characters from the longer word, if any
        result += word1[min_length:] + word2[min_length:]

        return result
