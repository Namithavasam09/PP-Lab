def binary_search(a,low,high,x):
    mid = low+high // 2
    while(low <= high):
        if (a[mid] == x):
            low = mid + 1
        if(a[mid] > x):
            high = mid
        if(a[mid] == x):
            return mid
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
