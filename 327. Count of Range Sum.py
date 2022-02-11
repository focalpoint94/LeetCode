class Solution:
    def countRangeSum(self, nums, lower, upper):
        sums = [0] * (len(nums) + 1)
        for i, num in enumerate(nums):
            sums[i+1] = sums[i] + num
        def ms(left, right):
            if left == right:
                return 0
            mid = (left + right) // 2
            count = ms(left, mid) + ms(mid+1, right)
            i, j = mid+1, mid+1
            for s in sums[left:mid+1]:
                while i <= right and sums[i] - s < lower:
                    i += 1
                while j <= right and sums[j] - s <= upper:
                    j += 1
                count += j - i
            sums[left:right+1] = sorted(sums[left:right+1])
            return count
        return ms(0, len(sums)-1)
