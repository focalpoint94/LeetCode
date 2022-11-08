from collections import defaultdict
class Solution:
    def longestDupSubstring(self, s: str) -> str:
        
        def rabinKarp(l, p=26, mod=10**9+7):
            nonlocal n
            h = 0
            for i in range(l):
                h = (h * p + arr[i]) % mod

            hashSet = set()
            hashSet.add(h)

            hashDict = defaultdict(list)
            hashDict[h].append(0)

            for i in range(1, n - l + 1):
                h = (h * p - arr[i-1] * pow(p, l, mod) + arr[i+l-1]) % mod
                if h in hashSet:
                    if any(arr[j:j+l] == arr[i:i+l] for j in hashDict[h]):
                        return i
                hashSet.add(h)
                hashDict[h].append(i)
            return False

        maxLen, ret = 0, ''
        n = len(s)
        arr = [ord(c) - ord('a') for c in s]
        low, high = 1, len(arr)
        while low <= high:
            mid = (low + high) // 2
            k = rabinKarp(mid)
            if k is not False:
                if mid > maxLen:
                    maxLen, ret = mid, s[k:k+mid]
                low = mid + 1
            else:
                high = mid - 1
        return ret
