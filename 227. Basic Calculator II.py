class Solution:
    def calculate(self, s: str) -> int:
        num, stack, sign = 0, [], '+'
        s += ' '
        for i, c in enumerate(s):
            if c.isdigit():
                num = num * 10 + int(c)
            elif i == len(s) - 1 or c != ' ':
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop()*num)
                elif sign == '/':
                    stack.append(int(stack.pop()/num))
                sign = c
                num = 0
        return sum(stack)
