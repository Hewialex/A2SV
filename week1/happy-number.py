class Solution:
    def isHappy(self, n: int) -> bool:
        k = str(n)
        if len(k) ==1:
            return k=="1" or k=="7"
        res = 0
        for num in k:
            res += int(num)**2
        return self.isHappy(res)