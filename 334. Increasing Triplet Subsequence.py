class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        dp = [nums[0]]
        for i in range(1, len(nums)):
            num = nums[i]
            insert_flag = False
            for j in range(len(dp)):
                if num <= dp[j]:
                    dp[j] = num
                    insert_flag = True
                    break
            if not insert_flag:
                dp.append(num)
            if len(dp) == 3:
                return True
        return False
