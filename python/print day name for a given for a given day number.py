#4.write a python program to print day name for a given for a given day number
def get_day_name(day_number):
    days=["sunday","monday","tuesday","wednesday","thursday","friday","saturday"]
    if 1<=day_number<=7:
        return days[day_number-1]
    else:
        return("Invalid day number please enter a number between 1 and 7")
day_num=int(input("enter a day number(1-7): "))
print("Day:",get_day_name(day_num))
