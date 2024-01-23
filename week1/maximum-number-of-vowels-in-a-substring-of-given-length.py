class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        maxCount = count = sum(ch in vowels for ch in s[:k])

        for i in range(k, len(s)):
            if s[i - k] in vowels:
                count -= 1
            if s[i] in vowels:
                count += 1
            maxCount = max(maxCount, count)

        return maxCount

            
            