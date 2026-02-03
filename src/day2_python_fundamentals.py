#Task-1: AGE IN 2030
print("TASK 1")
name1=input("What is your name?\n")
current_age=input("What is your current age?\n")
current_age=int(current_age)
age_2030= current_age+4
print(f"Hey {name1}, you will be {age_2030} years old in 2030!")

#Task-2: Bill Splitter
print("TASK 2")
num_people=input("Number of people:")
total=input("Total bill amount:")
num_people=int(num_people)
total=int(total)
billperperson=total/num_people
print(type(num_people))
print(type(total))
print(type(billperperson))
print(f"Total Bill={total}. Each person pays:{billperperson}")

#Task-3: The Raw Data formatter
print("TASK 3")
item_name="MacBook"
quantity=3
price=80000.5
in_stock= True
print(f"{item_name}, Qty:{quantity}, Price:{price}, Available:{in_stock}")
total_cost=quantity*price
print("Total cost:",total_cost)