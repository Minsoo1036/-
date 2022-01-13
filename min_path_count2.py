n, m = map(int,input().split())
d=[] #미로 상자
for i in range(n):
  d.append(list(map(int,input().split())))

from collections import deque
queue=deque()

dx = [-1,1,0,0] #상하좌우, 이동 패턴
dy = [0,0,-1,1]

def bfs(x,y): #x 행번호, y 열번호
  queue.append((0,0))

  while queue:
    x2,y2=queue.popleft()
    for i in range(4):
      nx = x2+dx[i]
      ny = y2+dy[i]

      if nx<0 or nx>n-1 or ny<0 or ny>m-1:
        continue

      if d[nx][ny]==1:
        d[nx][ny]=d[x2][y2]+1
        queue.append((nx,ny))

  return d[x][y]

print(bfs(n-1,m-1))

