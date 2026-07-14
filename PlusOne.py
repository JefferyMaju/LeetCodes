class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] != 9:
            digits[-1] += 1
            return digits
        elif digits[-1] == 9:
            num = 0
            for i in digits:
                num = num * 10 + i
            num += 1
            return [int(x) for x in str(num)]
