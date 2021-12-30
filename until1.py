'''
naive approach
'''
''''
n,k=map(int,input().split())
count=0
while n>1:
  if n%k==0:
    n=n/k
  else:
    n=n-1
  count+=1
print(count)
'''


n,k=map(int,input().split())
count=0
while True:
  target=n//k*k
  count+=n-target
  n=target
  count+=1
  n//=k
  if n<k:
    break


count+=(n-1)
print(count)


