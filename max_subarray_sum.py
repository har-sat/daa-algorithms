def max_crossing_subarray(array, l, mid, r):
  lsum = float('-inf')
  rsum = float('-inf')
  lmax = mid
  rmax = mid
  itr_sum = 0
  for i in range(mid, l - 1,-1):
    itr_sum += array[i]
    if itr_sum > lsum:
      lsum = itr_sum
      lmax = i

  itr_sum = 0
  for i in range(mid + 1, r + 1):
    itr_sum += array[i]
    if itr_sum > rsum:
      rsum = itr_sum
      rmax = i

  return lsum + rsum, lmax, rmax

def max_subarray_sum(array, l, r):
  if l == r:
    return array[l], l, r

  mid = (l + r) //2

  left_sum = max_subarray_sum(array, l, mid)
  right_sum = max_subarray_sum(array, mid+1, r)
  mid_sum = max_crossing_subarray(array, l, mid,  r)

  #max here is used like this:
  #     max(tup1, tup2, tup3, key=lambda x: x[0]) 
  return max(left_sum, right_sum, mid_sum)
  


array = list(map(int, input().strip().split()))
max_sum, l, r = max_subarray_sum(array, 0, len(array)-1)

print(max_sum, array[l:r+1])

