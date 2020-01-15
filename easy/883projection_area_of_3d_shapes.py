"""
On a N * N grid, we place some 1 * 1 * 1 cubes that are axis-aligned with the x, y, and z axes.

Each value v = grid[i][j] represents a tower of v cubes placed on top of grid cell (i, j).

Now we view the projection of these cubes onto the xy, yz, and zx planes.

A projection is like a shadow, that maps our 3 dimensional figure to a 2 dimensional plane.

Here, we are viewing the "shadow" when looking at the cubes from the top, the front, and the side.

Return the total area of all three projections.

Input: [[1,0],[0,2]]
Output: 8
Example 4:

Input: [[1,1,1],[1,0,1],[1,1,1]]
Output: 14
Example 5:

Input: [[2,2,2],[2,1,2],[2,2,2]]
Output: 21
"""


class Solution:
    def projectionArea(self, grid) -> int:
        ans = 0
        for cubes in grid:
            ans += len(cubes) - cubes.count(0)  # 'projection onto xy plane'
            ans += max(cubes)  # 'projection onto yz plane'
        zipped = zip(*list(grid))
        ys = list(zipped)
        for tup in ys:
            ans += max(tup)  # 'projection onto xz plane'
        return ans


if __name__ == '__main__':
    s = Solution()
    a = [[2, 2, 2], [2, 1, 2], [2, 2, 2]]
    res = s.projectionArea(a)
    print(res)
