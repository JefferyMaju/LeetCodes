class Solution(object):
    def checkPerfectNumber(self, num):
        if num%2 != 0: return False
        x = 1
        for i in range(2,int(num**0.5)+1):
            if num%i == 0:
                x += num//i
                x += i
            if x == num:
                b =  True
        if x != num: b = False
        return b
