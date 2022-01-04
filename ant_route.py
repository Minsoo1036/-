'''입력 예시 (1은 벽, 2는 먹이)
1 1 1 1 1 1 1 1 1 1
1 0 0 1 0 0 0 0 0 1
1 0 0 1 1 1 0 0 0 1
1 0 0 0 0 0 0 1 0 1
1 0 0 0 0 0 0 1 0 1
1 0 0 0 0 1 0 1 0 1
1 0 0 0 0 1 2 1 0 1
1 0 0 0 0 1 0 0 0 1
1 0 0 0 0 0 0 0 0 1
1 1 1 1 1 1 1 1 1 1
'''

box=[[0 for i in range(10)] for j in range(10)]

for i in range(10):
    box[i]=list(map(int,input().split())) #미로상자의 i번째 가로

x=1
y=1 #개미굴의 위치
box[x][y]=9 #시작점
while True:
    if box[x][y+1]!=1: #벽이 있는지 확인
        if box[x][y+1]==2:
            box[x][y+1]=9
            break #먹이 찾았으면 스톱.
        else:
            box[x][y+1]=9
            y+=1
    elif box[x+1][y]!=1:
        if box[x+1][y]==2:
            box[x+1][y]=9
            break #먹이 찾았으면 스톱.
        else:
            box[x+1][y]=9
            x+=1
    else: #벽을 만났으면 스톱
        break

for i in range(10):
    for j in range(10):
        print(box[i][j],end=" ")
    print()