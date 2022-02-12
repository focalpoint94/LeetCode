class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        arr = [nums[0]]
        for i in range(1, len(nums)):
            num = nums[i]
            insert_flag = False
            for j in range(len(arr)):
                if num <= arr[j]:
                    arr[j] = num
                    insert_flag = True
                    break
            if not insert_flag:
                arr.append(num)
            if len(arr) == 3:
                return True
        return False
