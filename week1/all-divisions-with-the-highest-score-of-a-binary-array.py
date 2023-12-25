from typing import List

class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        max_score = 0
        result_indices = []
        count_0 = nums.count(0)
        count_1 = nums.count(1)

        left_0 = 0
        left_1 = 0

        for i in range(len(nums) + 1):
            right_0 = count_0 - left_0
            right_1 = count_1 - left_1

            current_score = left_0 + right_1

            if current_score > max_score:
                max_score = current_score
                result_indices = [i]
            elif current_score == max_score:
                result_indices.append(i)

            if i < len(nums):
                if nums[i] == 0:
                    left_0 += 1
                else:
                    left_1 += 1

        return result_indices