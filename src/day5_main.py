#Task-1: Area & Perimeter
print("TASK 1")
length=int(input("Length of the rectangle:"))
breadth=int(input("Breadth of the rectangle:"))
def calc_rect(length,breadth):
    area=length*breadth
    perimeter=2*(length+breadth)
    return(area, perimeter)
ans=calc_rect(length,breadth)
print("Area:",ans[0])
print("Perimeter:",ans[1])

#Task-2: The logic library
import math_operations
print("TASK 2")
num_list=[10,22,21,11,44]
base=int(input("Enter base:"))
exp=int(input("Enter power:"))
print("Power=",math_operations.pow(base, exp))
print("Average=",math_operations.average(num_list))
