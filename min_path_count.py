#미로 탈출 (1,1) to (m,n), 0은 벽, 1은 길
from collections import deque

n,m = map(int,input().split())

d=[]
for i in range(n):
  d.append(list(map(int,input().split())))

#상하좌우 순 정의
dx=[-1,1,0,0] #행 변화량
dy=[0,0,-1,1] #열 변화량

def min_path_count(x,y): #입력값(1부터 시작)
  x=x-1
  y=y-1 #우리의 행렬, 0부터 시작
  queue = deque()
  queue.append((x,y))
  while queue:
    x,y=queue.popleft()

    for i in range(4):
      nx=x+dx[i]
      ny=y+dy[i]

      if nx<0 or ny<0 or nx>n-1 or ny>m-1:
        continue

      if d[nx][ny]==0:
        continue
      
      if d[nx][ny]==1: #처음 가보는 길이라면 ok, 이미 와봤던 장소라면 더 빠른 길 존재.
        d[nx][ny]=d[x][y]+1
        queue.append((nx,ny))

  return d[n-1][m-1]

print(min_path_count(1,1))



