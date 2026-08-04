class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        top, bot = 0, rows-1
        while top <= bot:
            mrow = (top + bot) // 2
            if target > matrix[mrow][-1]:
                top = mrow + 1
            elif target < matrix[mrow][0]:
                bot = mrow - 1
            else:
                break
        if top > bot:
            return False
        t, b = 0, cols-1
        while t <= b:
            m = (t + b) // 2
            if target < matrix[mrow][m]:
                b = m-1
            elif target > matrix[mrow][m]:
                t = m+1
            elif target == matrix[mrow][m]:
                return True
        if t>b:
            return False
