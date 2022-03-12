class Solution:
    def calculate(self, s: str) -> int:
        # ' ' is intentionally added,
        # to mark the end of the given string s
        # encountering ' ' will add the last number to the stack
        self.s = s + ' '
        self.ptr = 0
        return self.calc()
        
    def calc(self):
        num, stack, sign = 0, [], '+'
        while self.ptr < len(self.s):
            c = self.s[self.ptr]
            
            # if met with '(',
            # get the evaluated number by recursion
            if c == '(':
                self.ptr += 1
                num = self.calc()
            
            # deal with digits
            elif c.isdigit():
                num = num * 10 + int(c)
                self.ptr += 1
            
            # if met with operators or ')' or ' ',
            else:
                # if met with operators,
                # stack the number and update sign & num
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop()*num)
                elif sign == '/':
                    stack.append(int(stack.pop()/num))
                
                # if met with ')',
                # stack the number and return sum(stack)
                if c == ')':
                    self.ptr += 1
                    return sum(stack)
                
                sign = c
                num = 0
                self.ptr += 1
        
        return sum(stack)
