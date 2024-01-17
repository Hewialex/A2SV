class NumArray:

    def __init__(self, nums: List[int]):
        self.nums=[0]* len(nums)
        # ans =  sum(self.nums[left:right+1])
        self.nums[0] = nums[0]
        for i in range(1, len(nums)):
            self.nums[i] = self.nums[i-1] + nums[i]
        
    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.nums[right]
        else:
            return self.nums[right] - self.nums[left-1]


