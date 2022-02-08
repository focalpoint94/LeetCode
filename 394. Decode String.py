class Solution:
    def decodeString(self, s: str) -> str:
        return self.helper(s)
        
    def helper(self, s):
        if s.isalpha():
            return s
        ret = ''
        i = 0
        while i < len(s):
            if s[i].isdigit():
                num = int(s[i])
                i += 1
                while s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1
                temp_s = ''
                j = i + 1
                cnt = 1
                while True:
                    if s[j] == ']':
                        cnt -= 1
                    if s[j] == '[':
                        cnt += 1
                    if cnt == 0:
                        break
                    temp_s += s[j]      
                    j += 1
                ret += self.helper(temp_s) * num
                i = j + 1
            else:
                ret += s[i]
                i += 1
        return ret
