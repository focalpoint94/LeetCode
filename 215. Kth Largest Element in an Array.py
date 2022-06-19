class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq
        h = []
        for num in nums:
            if len(h) < k:
                heapq.heappush(h, num)
            else:
                heapq.heappush(h, num)
                heapq.heappop(h)
        return h[0]

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(left, right):
            rand_idx = random.randint(left, right)
            nums[rand_idx], nums[right] = nums[right], nums[rand_idx]
            pivot, j = nums[right], left
            for i in range(left, right):
                if nums[i] <= pivot:
                    nums[i], nums[j] = nums[j], nums[i]
                    j += 1
            nums[j], nums[right] = nums[right], nums[j]
            return j
        
        k = len(nums) - k
        left, right = 0, len(nums) - 1
        # left <= k <= right
        while left <= right:
            j = partition(left, right)
            if j > k:
                right = j - 1
            elif j < k:
                left = j + 1
            else:
                return nums[k]
