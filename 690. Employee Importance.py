"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        self.iddic = {}
        for employee in employees:
            self.iddic[employee.id] = employee
        self.totaldic = {}
        return self.calc(self.iddic[id])
        
    def calc(self, employee):
        if employee.id in self.totaldic:
            return self.totaldic[employee.id]
        total = employee.importance
        for sub in employee.subordinates:
            total += self.calc(self.iddic[sub])
        self.totaldic[employee.id] = total
        return total
