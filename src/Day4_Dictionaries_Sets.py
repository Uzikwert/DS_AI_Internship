#Task-1: The Personal Contact Book
print("TASK 1")
contacts={"Abdullah":1233453529,"Abia":9482108493,"Anas":2984118492}
contacts["Sudeep"]=9201928492
contacts["Abia"]=9382782929
print(contacts.get("Abdullah"))
print(contacts.get("Aejaz","Aejaz contact does not exist"))
for k in contacts:
    print(k,contacts[k])

#Task-2: The Duplicate Cleaner
print("TASK 2")
DupID=["ID01", "ID02", "ID01", "ID05", "ID02", "ID08", "ID01"]
unique_users=set(DupID)
print("Does ID05 exist?","ID05" in unique_users)
print(f"Length of original list:{len(DupID)} \nVS\nLength of unique list:{len(unique_users)}")
print("Number of Duplicates removed:",len(DupID)-len(unique_users))
print("Unique Users:",unique_users)

#Task-3: The interest Matcher
print("TASK 3")
friend_a={"Python", "Cooking", "Hiking", "Movies"}
friend_b={"Hiking", "Gaming", "Photography", "Python"}
print("Interests they both share are:",friend_a&friend_b)
print("Unique interests between the two are:",friend_a|friend_b)
print("Unique interests of a are:",friend_a-friend_b)
