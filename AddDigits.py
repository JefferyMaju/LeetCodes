class Solution(object):
    def addDigits(self, num):
        s = 0
        ss = 0
        for i in range(len(str(num))):
                s += num%10
                num = int(num/10)
        while len(str(s))>1:
            for i in range(len(str(s))):
                ss += s%10
                s = int(s/10)
            s = ss
            ss = 0
        return s
