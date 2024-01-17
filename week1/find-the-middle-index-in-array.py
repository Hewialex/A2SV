class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        prefix_sum = [0] * (len(nums) + 1)
        
        for i in range(len(nums)):
            prefix_sum[i+1] = prefix_sum[i] + nums[i]
        
        for i in range(len(nums)):
            left_sum = prefix_sum[i]
            right_sum = prefix_sum[len(nums)] - prefix_sum[i+1]
            
            if left_sum == right_sum:
                return i
            
        return -1
        # mid_idx = []
        # ans = 0
        # for i in range(len(nums)):
        #     ans += nums[i]
        #     mid_idx.append(ans)
        # if mid_idx[-1] - mid_idx[0] == 0:
        #     return 0
        # for j in range(1,len(mid_idx)-1):
        #     if mid_idx[j-1] == mid_idx[-1] - mid_idx[j]:
        #         return i - 1
        # if mid_idx[-2] == 0:
        #     return len(mid_idx) -1
            
        # return -1

