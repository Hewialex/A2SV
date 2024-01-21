class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        right = 0
        one_count = 0
        max_len = 0

        while right < len(nums):
            if nums[right] == 1:
                one_count += 1

            if (right - left + 1) - one_count > 1:
                if nums[left] == 1:
                    one_count -= 1
                left += 1

            max_len = max(max_len, right - left + 1)
            right += 1

        return max_len - 1