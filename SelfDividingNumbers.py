class Solution(object):
    def selfDividingNumbers(self, left, right):
        ans = []
        for i in range(left,right+1):
            flag = 0
            for x in str(i):
                if int(x) != 0:
                    if i%int(x) != 0:
                        flag = 1
                        break
                else: 
                    flag = 1
                    break
            if flag == 0:
                ans.append(i)
        return ans
        
