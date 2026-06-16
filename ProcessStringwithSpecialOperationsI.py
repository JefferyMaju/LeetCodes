class Solution(object):
    def processStr(self, s):
        x = ''
        for i in s:
            if i not in ["#","*","%"]:
                x += i
            elif i == "#":
                x += x
            elif i == "*":
                x = x[:-1:]
            elif i == "%":
                x = x[::-1]
        return x
        
