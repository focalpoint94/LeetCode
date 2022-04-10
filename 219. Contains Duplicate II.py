class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        numSet = set()
        j = 0
        for i in range(len(nums)):
            if i - j == k + 1:
                numSet.remove(nums[j])
                j += 1
            if nums[i] in numSet:
                return True
            numSet.add(nums[i])
        return False
