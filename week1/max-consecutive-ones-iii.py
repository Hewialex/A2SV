class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_ones = 0
        count = 0
        left = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                count += 1

            if count > k:
                if nums[left] == 0:
                    count -= 1
                left += 1

            max_ones = max(max_ones, right - left + 1)

        return max_ones
            