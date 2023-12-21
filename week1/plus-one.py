class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = int(''.join(map(str,digits)))
        ans = res+1 
        h = [int(ans) for ans in str(ans)]
        return h
