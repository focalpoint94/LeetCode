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
        self.generator = self.gen(nestedList)
        self.elem = None
        
    def gen(self, nestedList):
        for nl in nestedList:
            if nl.isInteger():
                yield nl.getInteger()
            else:
                yield from self.gen(nl.getList())
    
    def next(self) -> int:
        return self.elem
    
    def hasNext(self) -> bool:
        self.elem = next(self.generator, None)
        return True if self.elem != None else False
        

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
