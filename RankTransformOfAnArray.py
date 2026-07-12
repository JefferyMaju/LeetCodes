class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        x = sorted(arr)
        temp = {}
        y = []
        num = 0
        for i in range(len(x)):
            if x[i] == x[i-1] and i != 0:
                temp[x[i]] = temp[x[i-1]]
                num = temp[x[i]]
            else:
                temp[x[i]] = num+1
                num = temp[x[i]]
        for i in range(len(arr)):
            y.append(temp[arr[i]])
        return y
