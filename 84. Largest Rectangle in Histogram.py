class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ret = 0
        heights.append(0)
        stack = [-1]
        for i, h in enumerate(heights):
            while heights[stack[-1]] > h:
                j = stack.pop()
                w = i - stack[-1] - 1
                ret = max(ret, w * heights[j])
            stack.append(i)
        return ret
