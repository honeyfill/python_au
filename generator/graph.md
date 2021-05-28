# Graph

+ [Course Schedule II](#course-schedule-ii)
+ [Number Of Islands](#number-of-islands)
+ [Is Graph Bipartite](#is-graph-bipartite)
+ [Cheapest Flights Within k Stops](#cheapest-flights-within-k-stops)
+ [Shortest Path In Binary Matrix](#shortest-path-in-binary-matrix)
+ [Maximum Depth of N-ary Tree](#maximum-depth-of-n-ary-tree)
## Course Schedule II 

https://leetcode.com/problems/course-schedule-ii/

```python

from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if not numCourses: return []
        graph = {}
        for _to, _from in prerequisites:
            graph.setdefault(_from, []).append(_to)
        order = deque()
        visited, visiting = set(), set()
        def dfs(node):
            if node in visiting: return False
            visiting.add(node)
            res = True
            for child in graph.get(node, []):
                if child not in visited: res &= dfs(child)
                if not res: return False
            order.appendleft(node)
            visiting.discard(node)
            visited.add(node)
            return res
        for i in range(numCourses):
            if i not in visited:
                if not dfs(i): return []
        return list(order)
```
## Number Of Islands 

https://leetcode.com/problems/number-of-islands/

```python
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row, col = len(grid), len(grid[0])
        queue = deque([])
        count = 0
        for x in range(row):
            for y in range(col):
                if grid[x][y] == "1":
                    count+=1
                    queue.append((x,y))
                    self.bfs(grid, row, col, queue)
        return count

    def bfs(self, grid, row, col, queue):
        visited = set()
        while queue:
            x,y = queue.popleft()
            grid[x][y] = "visited"
            if (x,y) in visited: continue
            visited.add((x,y))
            for nx,ny in [[x+1,y],[x-1,y],[x,y+1],[x,y-1]]:
                if 0<=nx<row and 0<=ny<col and grid[nx][ny] == "1":
                    queue.append((nx,ny))
        
```
## Is Graph Bipartite 

https://leetcode.com/problems/is-graph-bipartite/

```python
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n,color = len(graph),{}
        def dfs(u):
            for v in graph[u]:
                if v not in color:
                    color[v] = 1 - color[u]
                    if not dfs(v): return False
                elif color[v] == color[u]:
                    return False
            return True
        for i in range(n):
            if i not in color and graph[i]:
                color[i] = 1
                if not dfs(i): return False
        return True
```
## Cheapest Flights Within k Stops 

https://leetcode.com/problems/cheapest-flights-within-k-stops/

```python
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        flight_list = defaultdict(list)
        for s,d,c in flights:
            flight_list[s].append([c,d])
        search_list = [(0,src,0)]

        while(search_list):
            distance, curr, stops = heapq.heappop(search_list) 
            if curr == dst:
                return distance
            elif stops > K:
                continue
            for cost, des in flight_list[curr]: 
                heapq.heappush(search_list, (distance+cost,des, stops+1))
        return -1
```
## Shortest Path In Binary Matrix 

https://leetcode.com/problems/shortest-path-in-binary-matrix/

```python
from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] != 0:
            return -1
        n = len(grid)
        if n == 1:
            if grid[0][0] == 0:
                return 1

        dq = deque()
        dq.append([0, 0])
        length = 1
        while dq:
            length += 1
            for _ in range(len(dq)):
                x, y = dq.popleft()
                for i in [-1, 0, 1]:
                    for j in [-1, 0, 1]:
                        if i == 0 and j == 0:
                            continue
                        if 0 <= x + i < n and 0 <= y + j < n and grid[x + i][y + j] == 0:
                            if x + i == n - 1 and y + j == n - 1:
                                return length
                            dq.append([x + i, y + j])
                            grid[x + i][y + j] = 1

        return -1
```
## Maximum Depth of N-ary Tree 

https://leetcode.com/problems/maximum-depth-of-n-ary-tree/

```python
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        
        nodes = deque()
        nodes.append((root, 1))
        maxix = 0
        while nodes:
            cur, val = nodes.popleft()
            maxix = val
            if cur.children:
                for child in cur.children:
                    nodes.append((child, val+1))
        return maxix
        
```
