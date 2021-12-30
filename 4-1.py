#find the coordinates of the last position

#1. naive version
l = int(input())
a = list(input().split()) # L R U D

x=1
y=1

for i in a:
  if i=="R":
    if x+1>=1 and x+1<=l:
      x+=1

  if i=="L":
    if x-1>=1 and x-1<=l:
      x-=1

  if i=="U":
    if y-1>=1 and y-1<=l:
      y-=1

  if i=="D":
    if y+1>=1 and y+1<=l:
      y+=1

print(y,x) #O(len(a))

#2. fix the motion in list, and do not repeat the same operation.
n=int(input())
x,y=1,1
plans=input().split()

dx = [0,0,-1,1]
dy = [-1,1,0,0]
move_types=['L','R','U','D'] #fixed motion

for plan in plans:
  for i in range(len(move_types)):
    if plan == move_types[i]: #check what plan is
      nx = x+dx[i]
      ny = y+dy[i] #potential coordinates

  if nx<1 or ny<1 or nx>n or ny>n:
    continue #not reflect the potential coordinates

  x,y = nx,ny #reflect the potential coordinates

print(x,y)


