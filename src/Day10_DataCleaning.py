#Task 1: The Integrity Audit
print("TASK 1")
import pandas as pd
df=pd.read_csv("customer_orders.csv")
print("Shape before:\n",df.shape)
print("Report of missing values:\n",df.isna().sum())
df["Price"]=df["Price"].fillna(df["Price"].median())
df["Name"]=df["Name"].fillna("Unknown")
df["Payment"]=df["Payment"].fillna(df["Payment"].mode()[0])
df["Date"]=df["Date"].fillna(df["Date"].mode()[0])
print("Duplicate rows:",df.duplicated().sum())
df=df.drop_duplicates()
print("Shape after:\n",df.shape)
print("After filling of missing values:\n",df.isna().sum())
print("Duplicate rows:",df.duplicated().sum())


#Task 2: The Type Fixer
print("TASK 2")
cf=pd.read_csv("customer_orders1.csv")
print(cf["Price"])
cf["Price"]=cf["Price"].str.replace('$','')
cf["Price"]=cf["Price"].str.replace(',','')
cf["Price"]=cf["Price"].astype(float)
cf["Date"]=pd.to_datetime(cf["Date"])
print("Data Types:\n",cf.dtypes)

#Task 3: The Categorical Standardizer
print("TASK 3")
print("Before string cleaning:\n",cf["Location"].unique())
cf["Location"]=cf["Location"].fillna(cf["Location"].mode()[0])
cf["Location"]=cf["Location"].str.strip()
cf["Location"]=cf["Location"].str.lower()
unique_loc=cf["Location"].unique()
print("After String Cleaning:\n",unique_loc)
