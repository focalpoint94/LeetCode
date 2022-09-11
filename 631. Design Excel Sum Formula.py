import itertools
class Excel:

    def __init__(self, height: int, width: str):
        # (row, col): (sum/cell, list/value)
        self.board = {}
        for i in range(26):
            for j in range(26):
                self.board[(i, j)] = ['cell', 0]

    def set(self, row: int, column: str, val: int) -> None:
        self.board[(row-1, ord(column)-65)] = ['cell', val]

    def get(self, row: int, column: str) -> int:
        r, c = row-1, ord(column)-65
        def _get(r, c):
            if self.board[(r, c)][0] == 'cell':
                return self.board[(r, c)][1]
            else:
                ret = 0
                for cell in self.board[(r, c)][1]:
                    ret += _get(cell[0], cell[1])
                return ret
        return _get(r, c)

    def sum(self, row: int, column: str, numbers: List[str]) -> int:
        cells = []
        for number in numbers:
            if ':' in number:
                colRow1, colRow2 = number.split(':')
                col1, row1 = ord(colRow1[0])-65, int(colRow1[1:])-1
                col2, row2 = ord(colRow2[0])-65, int(colRow2[1:])-1
                for c, r in itertools.product((i for i in range(col1, col2+1)), (i for i in range(row1, row2+1))):
                    cells.append((r, c))
            else:
                c, r = ord(number[0])-65, int(number[1:])-1, 
                cells.append((r, c))
        self.board[(row-1, ord(column)-65)] = ['sum', cells]
        return self.get(row, column)
        


# Your Excel object will be instantiated and called as such:
# obj = Excel(height, width)
# obj.set(row,column,val)
# param_2 = obj.get(row,column)
# param_3 = obj.sum(row,column,numbers)
