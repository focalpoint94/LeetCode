class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ret = 0
        stack = [-1]
        heights.append(0)
        for i, height in enumerate(heights):
            while height < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - 1 - stack[-1]
                ret = max(ret, h*w)
            stack.append(i)
        return ret
