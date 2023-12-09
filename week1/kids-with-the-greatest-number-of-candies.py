class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        result = []
        
        for i in range(len(candies)):
            total_candies = candies[i] + extraCandies
            result.append(total_candies >= max_candies)
        
        return result      