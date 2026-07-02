from collections import deque
class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m=len(grid)
        n=len(grid[0])
        dist=[[-2]*n for _ in range(m) ]
        q=deque([(0,0)])
        if grid[0][0]==1:
            dist[0][0]=health-1
            if dist[0][0]<=0:
                return False
        else:
            dist[0][0]=health
    
        while q:
            i,j=q.popleft()
            if i==m-1 and j==n-1:
                return True
            for x,y in (i-1,j),(i+1,j),(i,j-1),(i,j+1):
                if x>=0 and x<m and y<n and y>=0 and dist[x][y]==-2:
                    if grid[x][y]==1 :
                        cost=1
                    else:
                        cost=0
                    new_health=dist[i][j]-cost
                    if new_health>0 and new_health>dist[x][y]:
                        dist[x][y]=new_health
                        if cost==0:
                            q.appendleft((x,y))
                        else:
                            q.append((x,y))

        return False
        
                
                    
        