class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        v = [[0]*n for _ in range(m)]
        for i,j in walls:
            v[i][j] = -1 
        for i,j in guards:
            v[i][j] = 1

        for r,c in guards:
            sr = r-1
            while sr >= 0:
                print(sr, r)
                if v[sr][c] == -1 or v[sr][c] == 1:
                    break
                v[sr][c] = 2
                sr -= 1

            sr = r+1
            while sr < m :
                if v[sr][c] == -1 or v[sr][c]==1:
                    break
                v[sr][c] = 2
                sr += 1

            sc = c-1
            while sc >= 0:
                if v[r][sc] == -1 or v[r][sc] == 1:
                    break
                v[r][sc] = 2
                sc-=1
            sc = c+1
            while sc < n:
                print(r, sc)
                if v[r][sc] == -1 or v[r][sc] == 1:
                    break
                v[r][sc] = 2
                sc +=1 
        
        print(v)
        count = 0

        for i in range(m):
            for j in range(n):
                if v[i][j] == 0:
                    count+=1
               
        return count

