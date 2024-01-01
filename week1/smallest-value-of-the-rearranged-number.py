class Solution:
    def smallestNumber(self, num: int) -> int:
        if num == 0:
            return 0
        
        isNeg, nums, countZero, s = False, [], 0, str(num)
        
        if  num < 0:
            isNeg = True
            s = s[1:]
        
        for i in range(len(s)):
            if s[i] != '0':
                nums.append(s[i])
            else:
                countZero += 1

        nums.sort(reverse=isNeg)
        newN = ''.join(nums)

        if isNeg:
            return int('-' + newN + '0' * countZero)

        return int(newN[0] + '0' * countZero + newN[1:])
    
        