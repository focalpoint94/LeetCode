class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        rows, cols = [0] * 3, [0] * 3
        diags = [0] * 2
        for i, (y, x) in enumerate(moves):
            if i % 2 == 0:
                rows[y] += 1
                cols[x] += 1
                if y == x:
                    diags[0] += 1
                if y + x == 2:
                    diags[1] += 1
                if rows[y] == 3 or cols[x] == 3 or diags[0] == 3 or diags[1] == 3:
                    return 'A'
            else:
                rows[y] -= 1
                cols[x] -= 1
                if y == x:
                    diags[0] -= 1
                if y + x == 2:
                    diags[1] -= 1
                if rows[y] == -3 or cols[x] == -3 or diags[0] == -3 or diags[1] == -3:
                    return 'B'
        return 'Draw' if len(moves) == 9 else 'Pending'
