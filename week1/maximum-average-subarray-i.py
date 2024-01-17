class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        wind_sum = sum(nums[:k])
        max_sum = wind_sum

        for i in range(k,len(nums)):
            wind_sum += nums[i] - nums[i-k]
            max_sum = max(max_sum , wind_sum)
        return max_sum / k