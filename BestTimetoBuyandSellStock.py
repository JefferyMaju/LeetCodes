class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = prices[0]
        p = 0
        for i in prices:
            if i < l:
                l = i
            elif i > l:
                if (i-l) > p:
                    p = i-l
        return p
