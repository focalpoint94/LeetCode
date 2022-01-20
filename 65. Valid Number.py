class Solution:
    def isNumber(self, s: str) -> bool:
        import re
        pat = re.compile('(^[+-]?((\d+(\.\d*)?)|(\.\d+))$)|(^[+-]?((\d+(\.\d*)?)|(\.\d+))[eE][+-]?\d+$)')
        return re.match(pat, s)


class Solution:
    def isNumber(self, s: str) -> bool:
        dfa = [
            {"sign": 2, "dot": 3, "digit": 1},
            {"digit": 1, "expo": 5, "dot": 4},
            {"digit": 1, "dot":3},
            {"digit": 4},
            {"digit": 4, "expo": 5},
            {"sign": 6, "digit": 7},
            {"digit": 7},
            {"digit": 7},
        ]
        current_state =0
        for char in s:
            typ = ''
            if char.isdigit():
                typ = 'digit'
            elif char == '.':
                typ = 'dot'
            elif char in ['e', 'E']:
                typ = 'expo'
            elif char in ['+', '-']:
                typ = 'sign'
            else:
                return False
            if typ not in dfa[current_state]:
                return False
            current_state = dfa[current_state][typ]
        return current_state in [1, 4, 7]
