class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        # Define parents list for find/union parent operations
        parents = [i for i in range(26)]
        
        # find parent operation
        def find_parent(node):
            if node == parents[node]:
                return node
            parents[node] = find_parent(parents[node])
            return parents[node]
        
        # union parent operation
        def union_parent(node1, node2):
            node1 = find_parent(node1)
            node2 = find_parent(node2)
            if node1 <= node2:
                parents[node2] = node1
            else:
                parents[node1] = node2
        
        # For all equalities: apply 'union parent opt'
        # We'll later deal with unequalities
        unequals = []
        for equation in equations:
            if equation[1] == '!':
                unequals.append(equation)
            else:
                node1, node2 = ord(equation[0]) - ord('a'), ord(equation[3]) - ord('a')
                union_parent(node1, node2)
        
        # Make sure every node has its eldest parent
        for node in range(26):
            find_parent(node)
        
        # Now deal with unequalities:
        # If they have the same parent, it's a contradiction
        for equation in unequals:
            node1, node2 = ord(equation[0]) - ord('a'), ord(equation[3]) - ord('a')
            if parents[node1] == parents[node2]:
                return False
        return True
