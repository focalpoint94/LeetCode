from collections import Counter
from itertools import permutations
class Solution:
    def largestVariance(self, s: str) -> int:
        ret = 0
        c = Counter(s)

        for a, b in permutations(c, 2):
            ra, rb = c[a], c[b]
            if a != b:
                freq1, freq2 = 0, 0
                for char in s:
                    if char == a:
                        freq1 += 1
                        ra -= 1
                    elif char == b:
                        freq2 += 1
                        rb -= 1
                    else:
                        continue
                    
                    '''
                    why below condition fails?
                    example: ljpdkaaa
                    code with below condition will return 0
                    '''
                    # if freq1 < freq2:
                    #     freq1, freq2 = 0, 0

                    if freq1 < freq2 and rb != 0:
                        freq1, freq2 = 0, 0

                    if freq1 > 0 and freq2 > 0 :
                        ret = max(ret, freq1 - freq2)

        return ret
