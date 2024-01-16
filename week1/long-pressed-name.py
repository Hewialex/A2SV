class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        r , l = 0 , 0
        n , m  = len(name) , len(typed)

        while  r < m:
            if l < n and name[l] == typed[r]:
                l += 1
                r += 1
            elif  r > 0 and typed[r] == typed[r-1]:
                r += 1
            else:
                return False
        return l == n

        