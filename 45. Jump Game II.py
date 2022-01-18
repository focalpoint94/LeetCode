class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        now, jump = 0, 0
        while True:
            if now + nums[now] >= len(nums) - 1:
                return jump + 1
            val, next_idx = -1, -1
            for i in range(now+1, min(now+nums[now]+1, len(nums))):
                if i + nums[i] > val:
                    val = i + nums[i]
                    next_idx = i
            now = next_idx
            jump += 1
