class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        from collections import Counter
        c1 = Counter(nums1)
        c2 = Counter(nums2)
        ret = []
        for k in c2.keys():
            ret.extend([k] * min(c1[k], c2[k]))
        return ret
