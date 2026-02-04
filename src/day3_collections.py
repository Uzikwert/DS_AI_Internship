#Task-1: Inventory Manager
print("TASK 1")
inventory=["Apples","Bananas","Carrots","Dates"]
print("Current Iventory",inventory)
inventory.append("Eggs")
inventory.remove("Bananas")
print(inventory)

#Task-2: The Data Slicer
print("TASK 2")
temperatures = [22, 24, 25, 28, 30, 29, 27, 26, 24, 22]
print(temperatures[0])
print(temperatures[-1])
print("Afternoon Peak Temperatures:",temperatures[3:6])
print("Temperatures of the last three hours:",temperatures[-3:])

#Task-3: The Immutable Config
print("TASK 3")
screen_res=(1920,1080)
print(f"Current Resolution:{screen_res}")
#screen_res[0]=1280
print("Tuple cannot be modified!")
