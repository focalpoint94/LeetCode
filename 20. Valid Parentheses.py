class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for p in s:
            if p == '(' or p == '{' or p == '[':
                stack.append(p)
            else:
                if p == ')':
                    if not stack or stack[-1] != '(':
                        return False
                    else:
                        stack.pop()
                elif p == '}':
                    if not stack or stack[-1] != '{':
                        return False
                    else:
                        stack.pop()
                else:
                    if not stack or stack[-1] != '[':
                        return False
                    else:
                        stack.pop()
        if stack:
            return False
        return True
