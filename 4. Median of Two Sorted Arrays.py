INF = int(1e9)
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        if m > n:
            nums1, nums2, m, n = nums2, nums1, n, m
        
        left, right, p = 0, m, (m+n+1) // 2
        while left <= right:
            p1 = (left + right) // 2
            p2 = p - p1
            
            maxleft1 = -INF if p1 == 0 else nums1[p1-1]
            minright1 = INF if p1 == m else nums1[p1]
            
            maxleft2 = -INF if p2 == 0 else nums2[p2-1]
            minright2 = INF if p2 == n else nums2[p2]
            
            if maxleft1 <= minright2 and maxleft2 <= minright1:
                if (m + n) % 2 == 0:
                    return (max(maxleft1, maxleft2) + min(minright1, minright2))/2.
                return max(maxleft1, maxleft2)
            
            elif maxleft1 > minright2:
                right = p1 - 1
            
            else:
                left = p1 + 1
