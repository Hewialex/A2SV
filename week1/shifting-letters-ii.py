class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        prefix = [0] * (n+1)

        for start, end, d in shifts:
            if d == 1:
                prefix[start] += 1
                prefix[end + 1] -= 1
            else:
                prefix[start] -= 1
                prefix[end + 1] += 1
        for i in range(1, n+1):
            prefix[i] += prefix[i-1]

        ans = []
        orda = ord('a')

        for i, c in enumerate(s):
            cur = (ord(c) - orda + prefix[i]) % 26
            ans.append(chr(cur + orda))
        return "".join(ans)