class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []
        p_count = defaultdict(int)
        window_count = defaultdict(int)

        for char in p:
            p_count[char] += 1

        left = right = 0
        while right < len(s):
            window_count[s[right]] += 1

            if right - left + 1 > len(p):
                window_count[s[left]] -= 1
                if window_count[s[left]] == 0:
                    del window_count[s[left]]
                left += 1

            if window_count == p_count:
                result.append(left)

            right += 1

        return result
            