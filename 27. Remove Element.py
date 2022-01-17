class Solution:
    def removeElement(self, nums: List[int], val: int) -> int: 
        length = len(nums)
        i = 0
        while i <= length - 1:
            if nums[i] == val:
                nums[i], nums[length-1] = nums[length-1], nums[i]
                length -= 1
            else:
                i += 1
        return length
