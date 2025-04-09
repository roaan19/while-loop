m=int(input("enter the number"))
sum=0
temp=m

while temp>0:
    dight=temp%10
    sum=sum+dight**3
    temp=temp//10

if m==sum:
    print("it is an armstrong number ")
else :
    print("it is not an armstrong number")