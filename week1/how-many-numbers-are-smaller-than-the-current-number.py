class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        test = sorted(nums)
        ans = []
        for i in nums:
            ans.append(test.index(i)) 
        return ans  