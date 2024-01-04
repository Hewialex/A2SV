class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        sorted_lst = sorted(points,key=lambda x:sqrt(x[0]*x[0]+x[1]*x[1]))
        res =[]
        for i in range(k):
            res.append(sorted_lst[i])
        return res
        # for x,y in sorted_lst:
         

            