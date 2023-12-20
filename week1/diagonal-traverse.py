class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        diagonals = defaultdict(list) 
        res = []
        for m in range(len(mat)):
            for n in range(len(mat[0])):
                diagonals[m+n].append(mat[m][n])

        for sum_ , num in diagonals.items() :
            if sum_%2 == 0:
                res.extend(num[::-1])
            else:
                res.extend(num)

        return res  