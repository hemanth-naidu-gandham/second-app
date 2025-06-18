def search():
    flower={"rose":["white","red"],"lilly":["purple","red"]}
    name=input("enter a flower name:").lower()
    if name in flower:
        print(flower[name])
    else:
        print("not found")
search()