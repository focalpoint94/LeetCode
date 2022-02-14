class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def count(val):
            cnt = 0
            temp = 0
            for weight in weights:
                if temp + weight <= val:
                    temp += weight
                else:
                    cnt += 1
                    temp = weight
            return cnt + 1
        
        ret = sum(weights)
        left, right = max(weights), sum(weights)
        while left <= right:
            mid = (left + right) // 2
            if count(mid) <= days:
                ret = min(ret, mid)
                right = mid - 1
            else:
                left = mid + 1
        return ret
