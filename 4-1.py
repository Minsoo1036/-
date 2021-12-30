#find the coordinates of the last position

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



