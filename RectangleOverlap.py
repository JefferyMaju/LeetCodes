class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        x1 = max(rec1[0],rec2[0])
        y1 = max(rec1[1],rec2[1])
        x2 = min(rec1[2],rec2[2])
        y2 = min(rec1[3],rec2[3])

        if x1<x2 and y1<y2:
            return True
        else:
            return False
        
        # x(start) = max(x1A, x1B)
        # y(start) = max(y1A, y1A)
        # x(end) = min(x2A, x2B)
        # y(end) = min(y2A, y2B)
        # if x(start) < x(end) and y(start) < y(end): it overlaps
