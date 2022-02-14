class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict
        dic = defaultdict(int)
        for num in nums:
            dic[num] += 1
        import heapq
        h = []
        for key, val in dic.items():
            if len(h) < k:
                heapq.heappush(h, (val, key))
            else:
                heapq.heappushpop(h, (val, key))
        ret = []
        for val, key in h:
            ret.append(key)
        return ret
