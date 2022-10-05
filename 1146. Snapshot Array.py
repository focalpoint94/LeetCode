from bisect import bisect
class SnapshotArray:

    def __init__(self, length: int):
        # Time Complexity: O(N * logN)
        # Space Complexity: O(length)
        self.array = [[[0], [-1]] for i in range(length)]
        self.snap_id = 0
        self.changes = {}

    def set(self, index: int, val: int) -> None:
        self.changes[index] = val

    def snap(self) -> int:
        for index, value in self.changes.items():
            self.array[index][0].append(value)
            self.array[index][1].append(self.snap_id)
        self.changes = {}
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        j = bisect(self.array[index][1], snap_id)
        return self.array[index][0][j-1]
        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
