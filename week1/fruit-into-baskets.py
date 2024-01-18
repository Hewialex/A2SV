class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        ans = 0
        diction = defaultdict(int)
        l = 0
        
        for r in range(len(fruits)):
            diction[fruits[r]] += 1

            while len(diction) > 2 :
                diction[fruits[l]] -= 1
                if diction[fruits[l]] == 0:
                    del diction[fruits[l]]
                l += 1

            ans = max(r-l+1,ans)
        return ans



        