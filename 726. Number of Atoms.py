class Solution:
    def countOfAtoms(self, formula: str) -> str:
        import re
        from collections import Counter
        pattern = (r"([A-Z][a-z]*)(\d*)|(\()|(\))(\d*)")
        parse = re.findall(pattern, formula)
        stack = [Counter()]
        for name, freq1, left, right, freq2 in parse:
            if name:
                stack[-1][name] += int(freq1 or 1)
            elif left:
                stack.append(Counter())
            else:
                c = stack.pop()
                for k in c:
                    stack[-1][k] += c[k] * int(freq2 or 1)
        ret = ''
        for k in sorted(stack[0].keys()):
            if stack[0][k] == 1:
                ret += k
            else:
                ret += k
                ret += str(stack[0][k])
        return ret

# class Solution:
#     def countOfAtoms(self, formula: str) -> str:
#         from collections import Counter
#         N = len(formula)
#         stack = [Counter()]
#         i = 0
#         while i < N:
#             if formula[i] == '(':
#                 stack.append(Counter())
#                 i += 1
#             elif formula[i] == ')':
#                 i += 1
#                 j = i
#                 while i < N and formula[i].isdigit():
#                     i += 1
#                 freq = int(formula[j:i]) if formula[j:i] else 1
#                 c = stack.pop()
#                 for k, v in c.items():
#                     stack[-1][k] += v * freq
#             else:
#                 j = i
#                 i += 1
#                 while i < N and formula[i].islower():
#                     i += 1
#                 name = formula[j:i]
#                 j = i
#                 while i < N and formula[i].isdigit():
#                     i += 1
#                 freq = int(formula[j:i]) if formula[j:i] else 1
#                 stack[-1][name] += freq
#         ret = ''
#         for k in sorted(stack[0].keys()):
#             if stack[0][k] == 1:
#                 ret += k
#             else:
#                 ret += k
#                 ret += str(stack[0][k])
#         return ret
        
