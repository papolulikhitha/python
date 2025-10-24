mytuple=(10,18,'haha',True,45.5,"bob")
print(mytuple)
print(mytuple[2])
print(mytuple[-2])
print(mytuple[-1:2])
print(mytuple[ :-1])
mylist=list(mytuple) #changing tuple to mylist to modify
mylist.insert(2,45)
print(mylist)
