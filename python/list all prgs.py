mylist=[1,2,18,True,'lion',0.5]
print(mylist[3])
mylist.append('cse')
print(mylist)
mylist.insert(2,'aditya uni')
print(mylist)
mylist.remove(2)#removes numb 2 not position 2
print(mylist)
mylist.pop()#removes last charecter
print(mylist)
mylist.reverse()
print(mylist)

zoro=[7,'esther',99,0,False,'ironman']
print(zoro)
print(zoro[1:3])
print(zoro[-4:-1])
print(zoro[2:])
print(zoro[ :-1])
print(zoro[-4: ])


wow=['hasini',True,'lion',0.5,18,"apple"]
print(wow)
wow[3]="mango" #replaces 3rd  pos
print(wow)
wow[1:3]=["hello","hai"] #replaces two chars at 1 and 2 pos
print(wow)
for n in wow:
      print(n)#prints all elements in chars vertically
print('apple' in wow)#gives true if element is present in list


