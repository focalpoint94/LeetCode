class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic = {}
        # monotonicly increasing stack
        stack = []
        for num in nums2:
            while stack and stack[-1] < num:
                dic[stack.pop()] = num
            stack.append(num)
        
        ret = []
        for num in nums1:
            if num in dic:
                ret.append(dic[num])
            else:
                ret.append(-1)
        return ret
