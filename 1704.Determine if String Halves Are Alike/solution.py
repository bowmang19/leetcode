class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        counter1 = 0
        counter2 = 0
        first = s[0:len(s)//2]
        second = s[len(s)//2 if len(s) % 2 == 0
                   else ((len(s)//2)+1):]
        for i in first:
            if i.lower() in 'aeiou':
                counter1 += 1
        for i in second:
            if i.lower() in 'aeiou':
                counter2 += 1
        return counter1 == counter2
