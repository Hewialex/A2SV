class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        last_seen = {}
        max_length = 0
        left = 0
        right = 0

        while right < n:
            if s[right] in last_seen and last_seen[s[right]] >= left:
                left = last_seen[s[right]] + 1
            else:
                max_length = max(max_length, right - left + 1)
            
            last_seen[s[right]] = right
            right += 1

        return max_length