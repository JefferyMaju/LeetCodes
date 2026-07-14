class Solution:
    def isPalindrome(self, s: str) -> bool:
        x = ""
        flag = 0
        for i in s:
            if i.isalnum():
                x += i.lower()
        for i in range(len(x)//2):
            if x[i] != x[-i-1]:
                flag = 1
                break
        return True if flag == 0 else False
        
