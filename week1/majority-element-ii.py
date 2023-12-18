class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        count = n//3
        counter = Counter(nums)
        ans = []

        for num, freq in counter.items():
            if freq > count:
                ans.append(num)

        return ans
