numbers=input().split()
a=int(numbers[0])
b=int(numbers[1])
for i in range(0,5):
    if i==0:
        print(a+b)
    elif i==1:
        print(a-b)
    elif i==2:
        print(a*b)
    elif i==3:
        print(a//b)
    else:
        print(a%b)