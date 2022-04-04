# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        self.robot = robot
        self.visited = set()
        self.backTrack()
    
    def backTrack(self, cell=(0, 0), d=0):
        self.robot.clean()
        self.visited.add(cell)
        dy, dx = [-1, 0, 1, 0], [0, 1, 0, -1]
        for i in range(4):
            nowDir = (d + i) % 4
            nextCell = (cell[0] + dy[nowDir], cell[1] + dx[nowDir])
            if nextCell not in self.visited and self.robot.move():
                self.backTrack(nextCell, nowDir)
                self.goBack()
            self.robot.turnRight()
        
    def goBack(self):
        self.robot.turnRight()
        self.robot.turnRight()
        self.robot.move()
        self.robot.turnRight()
        self.robot.turnRight()
    
