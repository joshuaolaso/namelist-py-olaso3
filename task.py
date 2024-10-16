namelist = [
    ["david", "eve", "frank"],
    ["grace", "hedi", "ivan"],
    ["judy", "ken", "laura"],
    ["alice"],
    ]

for data in namelist:
    if "alice" in data:
        data.remove("alice")
        print(namelist)
else:
    name = input("enter new name: ")        
    namelist.append(name)
    print(namelist)