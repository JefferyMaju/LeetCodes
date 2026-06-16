class Solution(object):
    def fib(self, n):
        f = 0
        a = 0
        b = 1
        for i in range(0,n+1):
            f = f+a 
            a = b 
            b = f
        return f
        
