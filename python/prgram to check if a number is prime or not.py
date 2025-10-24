#1. write a python prgram to check if a number is prime or not?
n=int(input("enter the n value:"))
count=0
for i in range(2,n):
    if n%i==0:
        count=count+1
        break
    if count==0:
        print("primr number")
     else
        print("not a prime")


