from collections import defaultdict
class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        R,C= len(grid),len(grid[0])
        rows=defaultdict(int)
        for r in range(R):
            rows[r]=sum(grid[r])
        cols=defaultdict(int)
        for i,c in enumerate(list(zip(*grid))):# finding sum column wis
            cols[i]=sum(c)
        diff = [[0]*C for i in range(R)]
        for r in range(R):
            for c in range(C):
                diff[r][c]=rows[r]+cols[c]-(C-rows[r]+R-cols[c])
        return diff
