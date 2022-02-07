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

# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         k = len(nums) - k
#         low, high = 0, len(nums) - 1
#         while low < high:
#             j = self.partition(nums, low, high)
#             if j < k:
#                 low = j + 1
#             elif j > k:
#                 high = j - 1
#             else:
#                 return nums[k]
#         return nums[low]
        
#     def partition(self, nums, low, high):
#         rand_idx = random.randint(low, high)
#         nums[rand_idx], nums[high] = nums[high], nums[rand_idx]
#         pivot, left = nums[high], low
#         for i in range(low, high):
#             if nums[i] <= pivot:
#                 nums[i], nums[left] = nums[left], nums[i]
#                 left += 1
#         nums[left], nums[high] = nums[high], nums[left]
#         return left
