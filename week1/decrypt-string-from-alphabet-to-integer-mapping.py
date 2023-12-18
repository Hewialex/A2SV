class Solution:
    def freqAlphabets(self, s: str) -> str:

        answer = ""
        alphabets = "0abcdefghijklmnopqrstuvwxyz"

        i = 0 
        for i in range(len(s)): 

            if s[i] == "#":
                answer = answer[:-2]
                temp = (s[i- 2] + s[i - 1])
                answer += alphabets[int(temp)]
           
            else: 
                answer += alphabets[int(s[i])]

            i += 1
            
        return answer