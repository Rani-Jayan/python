a=input('enter the first string')
b=input('enter the second string')
x=a[1:2]
a=a.replace(a[1:2],b[1:2])
b=b.replace(b[1:2],x)
print("After swapping")
print(a,b)
