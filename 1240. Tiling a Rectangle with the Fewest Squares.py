class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        self.ret = n * m
        
        # using heights array and looking for minium height,
        # we are putting squares from the bottomleft
        def dfs(heights, moves):
            # all heights == n means that the rectangle is tiled
            if all(h == n for h in heights):
                self.ret = min(self.ret, moves)
                return
            # no need to search further
            if moves >= self.ret:
                return
            # looking for minimum height
            minH, minI = min(heights), heights.index(min(heights))
            # calculate maximum allowed width
            maxI = minI + 1
            while maxI < m and heights[maxI] == minH:
                maxI += 1
            # calculate maximum allowed length for a square
            maxLength = min(maxI-minI, n-minH)
            # consider all cases
            for length in range(maxLength, 0, -1):
                # putting a square
                for k in range(minI, minI+length):
                    heights[k] += length
                # go further
                dfs(heights, moves+1)
                # cancel the square
                for k in range(minI, minI+length):
                    heights[k] -= length
                    
        dfs([0] * m, 0)
        return self.ret
