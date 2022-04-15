class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        numJump, pos = 0, 0
        while True:
            if pos + nums[pos] >= len(nums) - 1:
                return numJump + 1
            nextPos, value = -1, -1
            for candidate in range(pos+1, min(pos+nums[pos]+1, len(nums))):
                if candidate + nums[candidate] > value:
                    nextPos, value = candidate, candidate + nums[candidate]
            numJump += 1
            pos = nextPos
