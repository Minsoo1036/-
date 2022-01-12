#얼음 과자 만들기.
n, m = map(int,input().split()) #행,열 길이

d=[] #ice box
for i in range(n):
  d.append(list(map(int,input().split())))



def dfs(x,y): #x:행번호, y:열번호
  if x<0 or x>n-1 or y<0 or y>m-1:
    return False

  if d[x][y]==0:
    d[x][y]=1
    dfs(x-1,y) #상하좌우 순
    dfs(x+1,y)
    dfs(x,y-1)
    dfs(x,y+1)
    return True #dfs가 실행되었다. = 얼음덩어리가 완성되었다.
  
  return False #dfs가 실행되지 않았다. = 새로 생긴 얼음덩어리가 없다.

result=0
for i in range(n):
  for j in range(m):
    if dfs(i,j) == True: #검사하는 시간복잡도 O(N)
      result+=1 #dfs수행하는 총 시간 복잡도 O(N)

  
print(result)



