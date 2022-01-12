'''
naive approach, 2<=n<=100,000, 2<=k<=100,000
'''
'''
n,k=map(int,input().split())
count=0
while n>1:
  if n%k==0:
    n=n/k
  else:
    n=n-1
  count+=1
print(count)
''' #O(klog_k_n), I guess this time complexity is right.

#reduce the counting number of minus operation
n,k=map(int,input().split()) 
count=0
while True:
  target=n//k*k #the core idea
  count+=n-target #just count at one time !
  n=target
  count+=1
  n//=k
  if n<k:
    break


count+=(n-1)
print(count) #O(log_k_n)


