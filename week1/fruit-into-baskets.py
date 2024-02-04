class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        max_fruits = 0
        left = 0
        right = 0
        counts = {}

        while right < len(fruits):
            counts[fruits[right]] = counts.get(fruits[right], 0) + 1
            right += 1

            while len(counts) > 2:
                counts[fruits[left]] -= 1
                if counts[fruits[left]] == 0:
                    del counts[fruits[left]]
                left += 1

            max_fruits = max(max_fruits, right - left)

        return max_fruits