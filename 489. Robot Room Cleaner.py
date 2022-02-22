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
        self.dy, self.dx = [-1, 0, 1, 0], [0, 1, 0, -1]
        self.backtrack(0, 0, 0)
        
    def backtrack(self, y, x, d):
        self.robot.clean()
        self.visited.add((y, x))
        for i in range(4):
            new_d = (d + i) % 4
            next_y, next_x = y + self.dy[new_d], x + self.dx[new_d]
            if (next_y, next_x) not in self.visited and self.robot.move():
                self.backtrack(next_y, next_x, new_d)
                self.robot.turnRight()
                self.robot.turnRight()
                self.robot.move()
                self.robot.turnRight()
                self.robot.turnRight()
            self.robot.turnRight()
