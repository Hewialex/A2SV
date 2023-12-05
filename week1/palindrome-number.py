class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x < 0: return False

        d = 1
        while x >= 10*d:
            d *= 10
        while x:
            r = x % 10
            l = x // d

            if l !=  r: return False
            x = (x % d) // 10
            d = d // 100
        return True

