n1 = int(input(" Enter first number :"))
n2 = int(input(" Enter second number :"))
n3 = int(input(" Enter third number :"))
n4 = int(input(" Enter fourth number :"))
if(n1>n2 and n1>n3 and n1>n4):
    print("First is the largest",n1)
elif(n2>n1 and n2>n3 and n1>n4):
    print("Second is the largest", n2)
elif(n3>n1 and n3>n2 and n1>n4):
    print("Third is the largest",n3)
else:
    print("Fourth is the largest",n4)