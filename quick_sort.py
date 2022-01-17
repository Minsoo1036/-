#Quick sort (퀵 정렬) , 호어 분할(Hoare Partition), O(N^2), but 기댓값 : O(NlogN)


array = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(array, start, end):
  if start>=end:
    return
  pivot = start #Hoare Partition
  left = start+1
  right = end
  while left <= right:
    while left <=end and array[left] <= array[pivot]: #왼쪽부터 pivot보다 큰 값을 찾음
      left+=1
    while right > start and array[right] >= array[pivot]: #오른쪽부터 pivot보다 작은 값을 찾음
      right-=1
    if left > right:
      array[right], array[pivot] = array[pivot], array[right]
    else:
      array[left], array[right] = array[right], array[left]

  quick_sort(array,start,right-1)
  quick_sort(array,right+1,end)

quick_sort(array,0,len(array)-1)
print(array)
