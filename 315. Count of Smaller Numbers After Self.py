class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        self.nums = nums
        self.count = [0] * len(nums)
        tobesorted = [i for i in range(len(nums))]
        self.merge_sort(tobesorted, 0, len(nums)-1)
        return self.count
        
    def merge_sort(self, arr, left, right):
        if left == right:
            return [arr[left]]
        mid = (left + right) // 2
        larr = self.merge_sort(arr, left, mid)
        rarr = self.merge_sort(arr, mid+1, right)
        pl, pr = 0, 0
        for i in range(left, right+1):
            if pl == len(larr):
                arr[i] = rarr[pr]
                pr += 1
            elif pr == len(rarr):
                arr[i] = larr[pl]
                self.count[arr[i]] += pr
                pl += 1
            elif self.nums[larr[pl]] <= self.nums[rarr[pr]]:
                arr[i] = larr[pl]
                self.count[arr[i]] += pr
                pl += 1
            else:
                arr[i] = rarr[pr]
                pr += 1
        return arr[left:right+1]
