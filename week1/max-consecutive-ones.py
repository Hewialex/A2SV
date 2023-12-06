

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        maxc = 0
        for num in nums:
            if num == 1:
                count += 1
                if count > maxc:
                    maxc = count
            else:
                count = 0
        return maxc

