class Solution:
    def lengthLongestPath(self, input: str) -> int:
        inp = input.split('\n') 
        ret = 0
        stack = [0]
        for i in range(0, len(inp)):
            address = inp[i]
            cnt = address.count('\t')
            name = address[cnt:]
            if cnt == 0:
                stack[0] = len(name)
            elif cnt == len(stack):
                stack.append(stack[-1]+len(name)+1)
            else:
                stack[cnt] = stack[cnt-1]+len(name)+1
            if '.' in name:
                ret = max(ret, stack[cnt])
        return ret
