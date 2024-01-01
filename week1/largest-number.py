class Solution:
    def largestNumber(self, nums: List[int]) -> str:  
        lis  = []

        for ele in nums:
            lis += [str(ele)]

        n = len(lis)
        for i in range(n):
            for j in range(i+1,n):

                if str(lis[i])+str(lis[j]) > str(lis[j]) + str(lis[i]):
                    continue
                else:
                    lis[i],lis[j] = lis[j],lis[i]
        ans = ''.join(lis)
        
        if int(ans) == 0:
            return "0"
        return ans