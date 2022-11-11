# Definition for a binary tree node.
class Node(object):
    def __init__(self, val=" ", left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
class Solution:
    def expTree(self, s: str) -> 'Node':
        tokens = deque(list(s))
        return self.parse_expression(tokens)

    def parse_expression(self, tokens):
        lhs = self.parse_term(tokens)
        while tokens and tokens[0] in ['+', '-']:
            op = tokens.popleft()
            rhs = self.parse_term(tokens)
            lhs = Node(val=op, left=lhs, right=rhs)
        return lhs

    def parse_term(self, tokens):
        lhs = self.parse_factor(tokens)
        while tokens and tokens[0] in ['*', '/']:
            op = tokens.popleft()
            rhs = self.parse_factor(tokens)
            lhs = Node(val=op, left=lhs, right=rhs)
        return lhs

    def parse_factor(self, tokens):
        # if integer
        if tokens[0].isnumeric():
            num = 0
            while tokens and tokens[0].isnumeric():
                num = num * 10 + int(tokens.popleft())
            return Node(val=str(num))

        elif tokens[0] == '(':
            # consume '('
            tokens.popleft()
            # if node is none: should raise error
            node = self.parse_expression(tokens)
            # consume ')'
            # if token is not ')': should raise error
            tokens.popleft()
            return node

        
