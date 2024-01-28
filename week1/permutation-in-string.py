class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        countS1 = Counter(s1)
        left = 0
        bothCount = 0

        for right in range(len(s2)):
            countS1[s2[right]] -= 1

            if countS1[s2[right]] >= 0:
                bothCount += 1

            if bothCount == len(s1):
                return True

            if right - left + 1 == len(s1):
                countS1[s2[left]] += 1

                if countS1[s2[left]] > 0:
                    bothCount -= 1

                left += 1

        return False