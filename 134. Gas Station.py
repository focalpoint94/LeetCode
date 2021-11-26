class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        culsum = 0
        for i in range(len(gas)):
            gas[i] -= cost[i]
            culsum += gas[i]
        if culsum < 0:
            return -1
        start_idx, culsum = 0, 0
        for i in range(len(gas)):
            culsum += gas[i]
            if culsum < 0:
                culsum = 0
                start_idx = i + 1
        return start_idx
