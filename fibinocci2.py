num=int(input("enter a number:"))
a=0
b=1
print("fibinocii series")
for i in range(num):
    print(a)
    c=a+b
    a=b
    b=c
