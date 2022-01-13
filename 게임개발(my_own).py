n,m = map(int,input().split())
x,y,d = map(int,input().split()) #시작 행, 열, 방향
maps = []
for i in range(n):
  maps.append(list(map(int,input().split()))) #게임 맵 입력

def turn_left():
  global d
  d-=1
  if d==-1:
    d=3

dx=[-1,0,1,0] #d=0,1,2,3 순
dy=[0,1,0,-1]

count=0
result=1 #겹치지 않게 이동한 칸의 수
maps[x][y]=2 #시작점 마크
while True:
  if count==4: #4번 다 회전했을때
    nx,ny=x-dx[d],y-dy[d]
    if maps[nx][ny] == 1: #바다의 경우 종료
      break #유일한 종료 조건
    if nx<0 or nx>m-1 or ny<0 or ny>n-1: #바다의 경우 종료
      break #유일한 종료 조건
    x,y=nx,ny
    count=0

  else: #4번 회전하기 전
    turn_left()
    count+=1
    nx=x+dx[d]
    ny=y+dy[d]

    if nx<0 or nx>m-1 or ny<0 or ny>n-1: #맵의 외곽은 바다
      continue

    if maps[nx][ny] == 0: #향하는 곳이 육지라면 이동.
      maps[nx][ny] = 2 #지나온 길 표시
      x,y=nx,ny
      count=0
      result+=1

print(result)

  




  

    
