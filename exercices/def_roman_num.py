class Solution:
    def romanToInt(self, roman_n):
        num = int()
        for n in range(len(roman_n)):
            if roman_n[n] == 'I':
                if n >= len(roman_n)-1:
                    num += 1
                elif roman_n[n] == 'I' and roman_n[n+1] == 'V' or roman_n[n] == 'I' and  roman_n[n+1] == 'X': 
                    num -= 1
                else:
                    num += 1
            elif roman_n[n] == 'V':
                num += 5
            elif roman_n[n] == 'X':
                if n >= len(roman_n)-1:
                    num += 10
                elif roman_n[n] == 'X' and roman_n[n+1] == 'L' or roman_n[n] == 'X' and roman_n[n+1] == 'C':
                    num -= 10
                    n+=1
                else:    
                    num += 10
            elif roman_n[n] == 'L':
                num += 50
            elif roman_n[n] == 'C':
                if n>= len(roman_n)-1:
                    num += 100
                elif roman_n[n] == 'C' and roman_n[n+1] == 'D' or roman_n[n] == 'C' and roman_n[n+1] == 'M':
                    num -= 100
                else:
                    num += 100
            elif roman_n[n] == 'D':
                num += 500
            else:
                num += 1000
        return num

print(Solution().romanToInt('MCMXCIV'))