from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ret = []
        q = deque()
        for i, num in enumerate(nums):
            # monotonicly descending deque (storing index)    
            while q and nums[q[-1]] <= num:
                q.pop()
            q.append(i)
            # if expired
            if q[0] == i - k:
                q.popleft()
            if i >= k - 1:
                ret.append(nums[q[0]])
        return ret
