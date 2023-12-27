class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sum = 0 
        for r in range(len(mat)):
            print(r)
            for c in range(len(mat[r])):
                if r == c or r+c == len(mat[r])-1:
                    sum += mat[r][c] 
        return sum    
           