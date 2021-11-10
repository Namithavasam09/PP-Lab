def binary_search(a,low,high,x):
    mid = low+high // 2
    if (a[mid] == x):
       return mid
    if(low <= high):
       if(a[mid] > x):
         return binary_search(a,mid+1,high,x)
       if(a[mid]>x):
         return binary_search(a,low,mid-1,n)
    return -1

n = int(input("enter the elements:"))
a = list(map(int,input("enter the elements").split()))
key = int(input("enter the element to be searched"))
low = 0
high = n-1
pos = binary_search(a,low,high,key)
if pos == -1:
   print("element not found")
else:
   print("element found at position",pos +1)
