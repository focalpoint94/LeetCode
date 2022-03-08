class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        if start.replace('X', '') != end.replace('X', ''):
            return False
        
        start_r_idx, start_l_idx = [], []
        end_r_idx, end_l_idx = [], []
        
        for idx, c in enumerate(start):
            if c == 'R':
                start_r_idx.append(idx)
            elif c == 'L':
                start_l_idx.append(idx)
        
        for idx, c in enumerate(end):
            if c == 'R':
                end_r_idx.append(idx)
            elif c == 'L':
                end_l_idx.append(idx)
        
        for i in range(len(start_r_idx)):
            if start_r_idx[i] > end_r_idx[i]:
                return False
        for i in range(len(start_l_idx)):
            if start_l_idx[i] < end_l_idx[i]:
                return False
        
        return True
