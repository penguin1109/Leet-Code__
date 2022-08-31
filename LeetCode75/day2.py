## Day 2: String

class Solution:
    def longestCommonPrefix(self, strs):
        ## Write a function to find the longest common prefix string amongst an array of strings
        answer = ""
        longest_length = 0
        temp_length = 0
        strs = sorted(strs, key = lambda x: len(x), reverse = False)
        start = 0
        for end in range(start, len(strs[0]) + 1):
            temp = strs[0][start:end]
            valid = True
            for s in strs[1:]:
                if temp != s[start:end]:
                    return answer
            if valid:
                answer = temp

        return answer
    
    def multiply(self, num1, num2):
        if len(num1) > len(num2):
            temp = num2
            num2 = num1
            num1 = temp
        answer = 0
        for n in range(len(num1)-1, -1, -1):
            mul = int(num1[n])
            answer += (mul * int(num2)) * (10 ** (len(num1) - n-1))

        return str(answer) 

                



        
        

