class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        slow, fast = nums[0], nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        p1, p2 = 0, slow
        while p1 != p2:
            p1 = nums[p1]
            p2 = nums[p2]
        return p1
