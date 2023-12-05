class Solution:
    def average(self, salary: List[int]) -> float:
        

        for i in salary:
            maxA = max(salary)
            minA = min(salary)
            salary.remove(maxA)
            salary.remove(minA)
            ans = sum(salary)/len(salary)
            return ans