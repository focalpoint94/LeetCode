class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        self.nums = nums
        self.count = [0] * n
        self.mergeSort([i for i in range(n)], 0, n-1)
        return self.count
        
    def mergeSort(self, arr, left, right):
        if left == right:
            return [arr[left]]
        mid = (left + right) // 2
        larr = self.mergeSort(arr, left, mid)
        rarr = self.mergeSort(arr, mid+1, right)
        pl, pr = 0, 0
        for i in range(left, right+1):
            if pl == len(larr):
                arr[i] = rarr[pr]
                pr += 1
            elif pr == len(rarr):
                arr[i] = larr[pl]
                self.count[larr[pl]] += pr
                pl += 1
            elif self.nums[larr[pl]] <= self.nums[rarr[pr]]:
                arr[i] = larr[pl]
                self.count[larr[pl]] += pr
                pl += 1
            else:
                arr[i] = rarr[pr]
                pr += 1
        return arr[left:right+1]
