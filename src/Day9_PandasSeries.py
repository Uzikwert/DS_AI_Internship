#Task 1: The Product Catalog
print("TASK 1")
import pandas as pd
values=pd.Series([700,150,300],index=['Laptop','Mouse','Keyboard'])
print("Price of Laptop:",values['Laptop'])
print(values[0:2])
print(values)
#Task 2: The Grade Filter
print("TASK 2")
import pandas as pd
grades=pd.Series([85,None,92,45,None,78,55])
print("Grades Series:\n",grades)
print("Null grades:\n",grades.isnull())
print("Grades Series after filling the missing grades:\n ",grades.fillna(0))
print("Grades greater than 60:\n",grades[grades>60])
#Task 3: The Username Formatter
print("TASK 3")
usernames=pd.Series([' Alice',' bOB ',' Charlie_Data',' daisy'])
a=usernames.str.strip()
b=a.str.lower()
print("Clean Series:\n",b)
print("Boolean result of the 'a' search",b.str.contains('a'))
