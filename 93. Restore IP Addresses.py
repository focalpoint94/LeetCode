class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        self.ret = []
        self.nums = set([str(i) for i in range(256)])
        self.helper(s, [])
        return self.ret
        
    def helper(self, s, ip):
        if len(ip) == 4:
            if not s:
                self.ret.append('.'.join(ip))
            return
        if not s:
            return
        
        for i in range(min(3, len(s))):
            if s[:i+1] in self.nums:
                self.helper(s[i+1:], ip+[s[:i+1]])
