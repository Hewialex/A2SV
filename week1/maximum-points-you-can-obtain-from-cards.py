class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        left = 0
        right = len(cardPoints) - k
        max_sum = sum(cardPoints[right:])
        curr_sum = max_sum
        
        for i in range(k):
            curr_sum = curr_sum - cardPoints[right] + cardPoints[left]
            max_sum = max(max_sum, curr_sum)
            left += 1
            right += 1
        
        return max_sum
            