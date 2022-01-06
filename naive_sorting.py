#sorting, O(N^2)
a,b,c=map(int,input().split())

li=[a,b,c]
l=len(li)

for i in range(l-1):
    mini=li[i]
    argmini=i
    for j in range(i+1,l,1):
        if mini>li[j]:
            mini=li[j]
            argmini=j
    li[argmini]=li[i]
    li[i]=mini
    
for i in li:
    print(i, end=" ")