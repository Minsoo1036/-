t=input()

row=int(t[1]) 
column=ord(t[0])-ord('a')+1 

#나이트가 이동할 수 있는 8가지 방향 정의 (c,r)순
steps = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(-1,2),(1,-2),(-1,-2)] 

result=0
for step in steps:
  next_row = row+step[1]
  next_column = column+step[0]

  if next_row>=1 and next_row<=8 and next_column>=1 and next_column <=8 :
    result+=1

print(result)