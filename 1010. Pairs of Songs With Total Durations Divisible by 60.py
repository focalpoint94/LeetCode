class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        time = [t % 60 for t in time]
        time.sort()
        ret = 0
        l, r = 0, len(time) - 1
        while l < r:
            if time[l] + time[r] == 60:
                if time[l] == 30:
                    cnt = 0
                    while  l <= len(time) - 1 and time[l] == 30:
                        cnt += 1
                        l += 1
                    ret += cnt * (cnt - 1) // 2
                    break
                else:
                    cnt1, cnt2 = 0, 0
                    l_val, r_val = time[l], time[r]
                    while time[l] == l_val:
                        cnt1 += 1
                        l += 1
                    while time[r] == r_val:
                        cnt2 += 1
                        r -= 1
                    ret += cnt1 * cnt2
            elif time[l] + time[r] < 60:
                l += 1
            else:
                r -= 1
        l, cnt = 0, 0
        while l <= len(time) - 1 and time[l] == 0:
            cnt += 1
            l += 1
        ret += cnt * (cnt - 1) // 2
        return ret
