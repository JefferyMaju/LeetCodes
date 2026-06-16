class Solution(object):
    def climbStairs(self, n):
        f = 0
        a = 1
        b = 0
        for i in range(0,n+1):
            f += a
            a = b
            b = f
        return f
        
