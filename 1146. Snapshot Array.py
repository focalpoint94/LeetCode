class SnapshotArray:
    from collections import defaultdict
    def __init__(self, length: int):
        self.array = defaultdict(dict)
        self.snap_id = 0
        
    def set(self, index: int, val: int) -> None:
        self.array[self.snap_id][index] = val

    def snap(self) -> int:
        self.snap_id += 1
        for idx in self.array[self.snap_id-1]:
            self.array[self.snap_id][idx] = self.array[self.snap_id-1][idx]
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        if index in self.array[snap_id]:
            return self.array[snap_id][index]
        return 0


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
