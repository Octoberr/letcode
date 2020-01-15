"""
A robot on an infinite grid starts at point (0, 0) and faces north.  The robot can receive one of three possible types of commands:

-2: turn left 90 degrees
-1: turn right 90 degrees
1 <= x <= 9: move forward x units
Some of the grid squares are obstacles.

The i-th obstacle is at grid point (obstacles[i][0], obstacles[i][1])

If the robot would try to move onto them, the robot stays on the previous grid square instead (but still continues following the rest of the route.)

Return the square of the maximum Euclidean distance that the robot will be from the origin.



Example 1:

Input: commands = [4,-1,3], obstacles = []
Output: 25
Explanation: robot will go to (3, 4)
Example 2:

Input: commands = [4,-1,4,-2,4], obstacles = [[2,4]]
Output: 65
Explanation: robot will be stuck at (1, 4) before turning left and going to (1, 8)


solution:
start at position x, y = 0, 0 and direction dx, dy = 0, 1
loop over commands
if command == -2, (dx, dy) -> (-dy, dx) ccw rotate 90 degree
if command == -1, (dx, dy) -> (dy, -dx) cw rotate 90 degree
if command 1-9, repeat given steps of x += dx, y += dy if not in obstacle, otherwise stop
"""


class Solution:
    def robotSim(self, commands, obstacles) -> int:
        x, y, dx, dy = 0, 0, 0, 1  # position & direction
        obstacles = set(map(tuple, obstacles))
        dis2 = 0

        for command in commands:
            if command == -2: dx, dy = -dy, dx  # ccw (left)
            if command == -1: dx, dy = dy, -dx  # cw (right)
            if 1 <= command <= 9:
                for _ in range(command):
                    if (x + dx, y + dy) in obstacles: break
                    x += dx
                    y += dy
                dis2 = max(dis2, x ** 2 + y ** 2)
        return dis2


if __name__ == '__main__':
    s = Solution()
    commands = [4, -1, 4, -2, 4]
    obstacles = [[2, 4]]
    res = s.robotSim(commands, obstacles)

