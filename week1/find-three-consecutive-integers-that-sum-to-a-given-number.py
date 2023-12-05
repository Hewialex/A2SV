class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        h = []
        if num%3 == 0:
            n = num//3
            h.append(n-1)
            h.append(n)
            h.append(n+1)
            return h
        else:
            return h