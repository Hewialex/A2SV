class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = []
        l = 0
        for i in range(len(nums)):
            l += nums[i]
            ans.append(l)
        return ans