class Solution(object):
    def categorizeBox(self, length, width, height, mass):
        bflag = 0
        hflag = 0
        if length >= 10**4 or  width >= 10**4 or height >= 10**4 or mass >= 10**4 or length*width*height >= 10**9:
            bflag = 1
        if mass >= 100:
            hflag = 1
        if bflag == 1 and hflag == 1:
            return "Both"
        elif bflag == 1 and hflag == 0:
            return "Bulky"
        elif hflag == 1 and bflag == 0:
            return "Heavy"
        else: return "Neither"
        
