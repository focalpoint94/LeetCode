class Solution:
    def numSquares(self, n: int) -> int:
        psns = []
        x = 1
        while x * x <= n:
            psns.append(x*x)
            x += 1
        
        nums, cnt = {n}, 0
        while nums:
            next_nums = set()
            cnt += 1
            for num in nums:
                for psn in psns:
                    if psn == num:
                        return cnt
                    if num < psn:
                        break
                    next_nums.add(num-psn)
            nums = next_nums
