

#2.write a program to display all prime numbers within an interval
start=int(input("Enter the start of the interval"))
end=int(input("Enter the end of the interval"))
print("Prime number between",start,"and",end,"are.")
for num in range(start,end+1):
    if num>1:
        for i in range(2,num):
          if num%i==0:
              break
          else:
              print(num)
