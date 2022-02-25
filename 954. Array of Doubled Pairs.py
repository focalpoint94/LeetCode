class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        from collections import defaultdict
        dic = defaultdict(int)
        n_pos, n_neg, n_zero = [], [], []
        for num in arr:
            dic[num] += 1
            if num > 0:
                n_pos.append(num)
            elif num == 0:
                n_zero.append(num)
            else:
                n_neg.append(num)
        
        if len(n_zero) % 2 != 0 or len(n_pos) % 2 != 0:
            return False
        
        n_pos.sort()
        n_neg.sort(reverse=True)
        
        for num in n_pos:
            if dic[num] != 0:
                if dic[2*num] <= 0:
                    return False
                dic[num] -= 1
                dic[2*num] -= 1
        for num in n_neg:
            if dic[num] != 0:
                if dic[2*num] <= 0:
                    return False
                dic[num] -= 1
                dic[2*num] -= 1
        return True
