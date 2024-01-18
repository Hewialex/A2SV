class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = 0
        prefix = 0
        prefix_count = [0] * k
        prefix_count[0] = 1
        
        for num in nums:
            prefix = (prefix + num) % k
            count += prefix_count[prefix]
            prefix_count[prefix] += 1
        
        return count
            