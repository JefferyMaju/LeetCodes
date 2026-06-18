class Solution(object):
    def reverseString(self, s):
        for i in range(-1,-(len(s)//2+1),-1):
            temp = s[i]
            s[i] = s[i*(-1)-1]
            s[i*(-1)-1] = temp
