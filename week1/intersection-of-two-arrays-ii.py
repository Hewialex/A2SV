class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count1 = {}
        count2 = {}
        for num in nums1:
            count1[num] = count1.get(num, 0) + 1
        for num in nums2:
            count2[num] = count2.get(num, 0) + 1
        
        arr = []
        for num in count1:
            if num in count2:
                count = min(count1[num], count2[num])
                arr.extend([num] * count)
        
        return arr