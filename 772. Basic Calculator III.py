class Solution:
    def calculate(self, s: str) -> int:
        self.s = s + ' '
        self.ptr = 0
        return self.helper()
    
    def helper(self):
        stack, num, sign = [], 0, '+'
        while self.ptr < len(self.s):
            char = self.s[self.ptr]
            if char.isdigit():
                num = num * 10 + int(char)
                self.ptr += 1
            elif char in ['+', '-', '*', '/', ' ']:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop()*num)
                else:
                    stack.append(int(stack.pop()/num))
                sign = char
                num = 0
                self.ptr += 1
            elif char == ')':
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop()*num)
                else:
                    stack.append(int(stack.pop()/num))
                self.ptr += 1
                return sum(stack)
            else:
                self.ptr += 1
                num = self.helper()
        return sum(stack)
        
        
