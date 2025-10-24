class car:
    def __init__(int ,make,model,year,color):
        int.make=make
        int.model=model
        int.year=year
        int.color=color
        int.speed=0 #default value
        
        #creating instances/objects for class
car1=car("ford","mustang",1969,"black")
car2=car("porshe","718 boxter",2006,"blue")
print(car1.make)
print(car1.speed)
