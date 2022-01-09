#상하좌우 문제
n = int(input())
plans = list(input().split())

move_types=['R','L','U','D']
dc=[1,-1,0,0]
dr=[0,0,-1,1] #변화량 정의

c=1 #column
r=1 #row
for plan in plans:
  for i in range(len(move_types)):
    if plan == move_types[i]:
      nc=c+dc[i]
      nr=r+dr[i]
  
  if nc<1 or nc>n or nr<1 or nr>n:
    continue

  c,r=nc,nr

print(r,c)


