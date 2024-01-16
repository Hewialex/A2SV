class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        n = len(skill)
        l = 0
        r = n -1
        sum_skill = 0
        while l < r:
            if skill[l] + skill[r] == skill[l+1] + skill[r-1]:
                sum_skill += skill[l] * skill[r]
                l += 1
                r -= 1
            else:
                return -1
        return sum_skill


       