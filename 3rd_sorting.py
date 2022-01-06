#점수가 세번째로 큰 학생, O(3N)=O(N)

'''
5
minsu 78
gunho 64
sumin 84
jiwon 96
woosung 55
'''

n=int(input())
d=dict()
l=[]
for i in range(n):
    a,b=input().split()
    d[int(b)]=a
    l.append(int(b))
    
for i in range(3):
    maxi=l[i]
    argmaxi=i
    for j in range(i+1,n,1):
        if maxi<l[j]:
            argmaxi=j
            maxi=l[j]
    l[argmaxi]=l[i]
    l[i]=maxi
print(d[l[2]])