# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        def generator(nestedList):
            for nl in nestedList:
                if nl.isInteger():
                    yield nl.getInteger()
                else:
                    yield from generator(nl.getList())
        self.g = generator(nestedList)
        self.val = next(self.g, None)
    
    def next(self) -> int:
        ret = self.val
        self.val = next(self.g, None)
        return ret
    
    def hasNext(self) -> bool:
        return not(self.val is None)
        

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
