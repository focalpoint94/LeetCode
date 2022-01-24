class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1, p2 = m - 1, n - 1
        for i in range(m+n-1, -1, -1):
            p1_val = nums1[p1] if p1 >= 0 else -float('inf')
            p2_val = nums2[p2] if p2 >= 0 else -float('inf')
            if p1_val >= p2_val:
                nums1[i] = p1_val
                p1 -= 1
            else:
                nums1[i] = p2_val
                p2 -= 1
