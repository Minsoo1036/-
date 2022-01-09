n,m = map(int,input().split())
r,c,d = map(int,input().split()) #A,B,d 순
r+=1 #시작점 행 좌표 (나의 행렬 기준)
c+=1 #시작점 열 좌표 (나의 행렬 기준)

maps=[[0 for i in range(m)] for j in range(n)]

for i in range(n):
  maps[i]=list(map(int,input().split())) #맵 받기

marker_map = [[0 for i in range(m)] for j in range(n)]
#지나왔던 곳 표시

marker_map[r-1][c-1]=1

def turn_left():
  global d
  d-=1
  if d==-1:
    d=3

dr = [-1,0,1,0]
dc = [0,1,0,-1] #d=0,1,2,3 순

count=1
turn_time=0
while True:
  turn_left()
  nr=r+dr[d]
  nc=c+dc[d]

  if nr>=1 and nr<=n and nc>=1 and nc<=m and marker_map[nr-1][nc-1]==0 and maps[nr-1][nc-1]==0:
      marker_map[nr-1][nc-1]=1
      turn_time=0
      r,c=nr,nc
      count+=1
      continue
  else:
    turn_time+=1
  
  if turn_time==4:
    nr=r-dr[d]
    nc=c-dc[d]
    if maps[nr-1][nc-1]==0:
      #count+=1
      r,c=nr,nc
    else:
      break
    turn_time=0 #움직인 후에는 항상 turn_time 초기화

print(count)















