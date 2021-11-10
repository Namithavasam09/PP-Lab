def linear_search(a,n,x):
    n = n-1
    if (a[n] == x):
       return n
    if(n >= 0):
       return linear_search(a,n,x)
    return -1

n = int(input("enter the elements:"))
a = list(map(int,input("enter the elements").split()))
key = int(input("enter the element to be searched"))

pos = linear_search(a,n,key)
if pos == -1:
   print("element not found")
else:
   print("element found at position",pos +1)
