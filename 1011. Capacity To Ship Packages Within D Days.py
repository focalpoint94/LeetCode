class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        max_capacity = 0
        for w in weights:
            max_capacity += w
        
        ret = max_capacity
        l, r = 0, max_capacity
        while l <= r:
            capacity = (l + r) // 2
            if self.isEnoughCapacity(weights, capacity, days):
                ret = min(ret, capacity)
                r = capacity - 1
            else:
                l = capacity + 1
        return ret
    
    
    def isEnoughCapacity(self, weights, capacity, days):
        if capacity < max(weights):
            return False
        num_days = 1
        tempsum = 0
        for w in weights:
            tempsum += w
            if tempsum > capacity:
                num_days += 1
                tempsum = w
        return (num_days <= days)
