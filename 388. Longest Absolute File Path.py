class Solution:
    def lengthLongestPath(self, input: str) -> int:
        inp = input.split('\n')
        ret = 0
        stack = [0]
        for address in inp:
            lvl = address.count('\t')
            name = address.split('\t')[-1]
            if lvl == 0:
                stack[0] = len(name)
            elif lvl == len(stack):
                stack.append(stack[-1]+len(name)+1)
            else:
                stack[lvl] = stack[lvl-1]+len(name)+1
            if '.' in name:
                ret = max(ret, stack[lvl])
        return ret
