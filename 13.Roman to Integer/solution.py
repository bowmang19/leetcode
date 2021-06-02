class Solution:
    def romanToInt(self, s: str) -> int:
        num = 0
        roman = ["I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000]
        for i in len(s):
            if s[i] == 'I':
                if s[i+1] == 'V':
                    num += 4
                if s[i+1] == 'X':
                    num += 9
                else:
                    num += roman[s[i]]
            if s[i] == 'X':
                if s[i+1] == 'L':
                    num += 40
                if s[i+1] == 'C':
                    num += 90
                else:
                    num += roman[s[i]]
            if s[i] == 'C':
                if s[i+1] == 'D':
                    num += 400
                if s[i+1] == 'M':
                    num += 900
                else:
                    num += roman[s[i]]
            if


'''
iterate through
if current item is I and next is v -> 5
if current item is I and next is x -> 90
if current item is x and next is l -> 40
if current item is x and next is c -> 90


'''
