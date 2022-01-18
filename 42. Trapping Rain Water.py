class Solution:
    def trap(self, height: List[int]) -> int:
        ret = 0
        l, r = 0, len(height) - 1
        leftmax, rightmax = height[l], height[r]
        while r - l >= 2:
            curmax = max(leftmax, rightmax)
            if curmax == rightmax:
                l += 1
                if height[l] < leftmax:
                    ret += leftmax - height[l]
                leftmax = max(leftmax, height[l])
            else:
                r -= 1
                if height[r] < rightmax:
                    ret += rightmax - height[r]
                rightmax = max(rightmax, height[r])
        return ret
