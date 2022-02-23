class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        if p1 == p2:
            return False
        length = (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2
        if (p1[0] - p3[0])**2 + (p1[1] - p3[1])**2 > length:
            p2, p3 = p3, p2
        if (p1[0] - p4[0])**2 + (p1[1] - p4[1])**2 > length:
            p2, p4 = p4, p2
        length1 = (p1[0] - p3[0])**2 + (p1[1] - p3[1])**2
        length2 = (p1[0] - p4[0])**2 + (p1[1] - p4[1])**2
        if length1 != length2:
            return False
        length3 = (p2[0] - p3[0])**2 + (p2[1] - p3[1])**2
        length4 = (p2[0] - p4[0])**2 + (p2[1] - p4[1])**2
        if length3 != length4:
            return False
        if length3 != length1:
            return False
        return (p1[1]-p3[1])*(p1[1]-p4[1]) == -(p1[0]-p3[0])*(p1[0]-p4[0])
