database={}
for i in range(3):
    name=input("enter person name:")
    if name not in database:
        database[name]=[]
        n=int(input("enter your"))
        for k in range(n):
            interest = input("en")
            database[name].append(interest)
print(database)