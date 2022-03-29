class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        self.lower, self.upper = lower, upper
        n = len(nums)
        sums, prev = [0] * (n+1), 0
        for i in range(n):
            sums[i+1] = nums[i] + prev
            prev += nums[i]
        self.ret = 0
        self.mergeSort(sums, 0, n)
        return self.ret
        
    def mergeSort(self, sums, left, right):
        if left == right:
            return [sums[left]]
        mid = (left + right) // 2
        lsums = self.mergeSort(sums, left, mid)
        rsums = self.mergeSort(sums, mid+1, right)
        l, r = 0, 0
        for lval in lsums:
            while r < len(rsums) and rsums[r] - lval <= self.upper:
                r += 1
            while l < len(rsums) and rsums[l] - lval < self.lower:
                l += 1
            self.ret += r - l
        sums[left:right+1] = sorted(sums[left:right+1])
        return sums[left:right+1]
