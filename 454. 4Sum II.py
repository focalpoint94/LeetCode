class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        from collections import Counter
        c1 = Counter()
        c2 = Counter()
        for n1 in nums1:
            for n2 in nums2:
                c1[n1+n2] += 1
        for n3 in nums3:
            for n4 in nums4:
                c2[n3+n4] += 1
        ret = 0
        for k, v in c1.items():
            ret += c2[-k] * v
        return ret
