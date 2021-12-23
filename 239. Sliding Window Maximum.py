from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ret = []
        # q stores index
        q = deque()
        for i in range(len(nums)):
            while q and nums[q[-1]] <= nums[i]:
                q.pop()
            q.append(i)
            if q[0] == i - k:
                q.popleft()
            if i >= k - 1:
                ret.append(nums[q[0]])
        return ret
