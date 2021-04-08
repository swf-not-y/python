number = input("请输入一个自然数：>")
a=int(number)
while(a !=1):
    if(a%2 == 1):
        a=a*3+1
    else:
        a=a/2
print(a)
