class Solution:
    def countOfAtoms(self, formula: str) -> str:
        from collections import Counter
        N = len(formula)
        stack = [Counter()]
        i = 0
        while i < N:
            if formula[i] == '(':
                stack.append(Counter())
                i += 1
            elif formula[i] == ')':
                i += 1
                j = i
                while i < N and formula[i].isdigit():
                    i += 1
                freq = int(formula[j:i]) if formula[j:i] else 1
                c = stack.pop()
                for k, v in c.items():
                    stack[-1][k] += v * freq
            else:
                j = i
                i += 1
                while i < N and formula[i].isalpha() and formula[i].islower():
                    i += 1
                name = formula[j:i]
                j = i
                while i < N and formula[i].isdigit():
                    i += 1
                freq = int(formula[j:i]) if formula[j:i] else 1
                stack[-1][name] += freq
        ret = ''
        for k in sorted(stack[0].keys()):
            if stack[0][k] == 1:
                ret += k
            else:
                ret += k
                ret += str(stack[0][k])
        return ret
