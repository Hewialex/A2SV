class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        arr = []

        for i in range(len(nums)//2):
            frequency = nums[2*i]
            value = nums[2*i+1]

            arr += [value]*frequency
        return arr  