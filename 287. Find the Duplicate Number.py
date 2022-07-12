class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        cur = 0
        while cur != slow:
            slow = nums[slow]
            cur = nums[cur]
        return cur
