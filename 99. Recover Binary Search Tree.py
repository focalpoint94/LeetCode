class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        INF = pow(2, 31) + 1
        # self.reg1: fisrt error value
        # self.reg2: second error value
        self.reg1, self.reg2 = -INF, INF
        # found_flag: True if an error has been found
        self.found_flag = False
        # swap node1's & node2's value
        self.node1, self.node2 = None, None
        
        self.dfs(root)
        
        temp = self.node1.val
        self.node1.val = self.node2.val
        self.node2.val = temp
        
        
    def dfs(self, cur):
        if cur.left != None:
            self.dfs(cur.left)
            
        val = cur.val
        # if no error until now
        if not self.found_flag:
            # valid
            if val > self.reg1:
                self.reg1 = val
                self.node1 = cur
            # error
            else:
                self.found_flag = True
        if self.found_flag:
            if val < self.reg1:
                if val < self.reg2:
                    self.reg2 = val
                    self.node2 = cur
            else:
                return
        
        if cur.right != None:
            self.dfs(cur.right)
        
