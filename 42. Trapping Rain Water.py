class Solution:
    def trap(self, height: List[int]) -> int:
        ret = 0
        l, r = 0, len(height) - 1
        maxLeft, maxRight = height[0], height[-1]
        while l + 2 <= r:
            if height[l] <= height[r]:
                l += 1
                maxLeft = max(maxLeft, height[l])
                ret +=  max(min(maxLeft, maxRight) - height[l], 0)
            else:
                r -= 1
                maxRight = max(maxRight, height[r])
                ret += max(min(maxLeft, maxRight) - height[r], 0)
        return ret
