# First Code (Best in Complexity)
class Solution(object):
    def reverse(self,x):
        flag=0
        if x<0:
            flag = 1
            x = abs(x)
        res = int(str(x)[::-1])
        if flag==1:
            res *= -1
        if (res > (2**31)-1) or (res < -2**31): res = 0
        return res

# Second Code (Medium in Complexity)
class Solution(object):
    def reverse(self,x):
        res=0
        flag=0
        if x<0:
            flag = 1
            x = abs(x)
        for i in range(len(str(x))):
            res *= 10
            res += x%10
            x = int(x/10)
        if flag==1:
            res *= -1
        if (res > (2**31)-1) or (res < -2**31): res = 0
        return res

# Third Code (Worst in Complexity)
class Solution(object):
    def reverse(self,x):
        res = 0
        if x>=0:
            for i in range(len(str(x))):
                res *= 10
                res += x%10
                x = int(x/10)
        else:
            x *= -1
            for i in range(len(str(x))):
                res *= 10
                res += x%10
                x = int(x/10)
            res *= -1
        if (res > (2**31)-1) or (res < -2**31): res = 0
        return res
