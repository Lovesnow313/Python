

my_dict = { 1 : "apple", 2 : "ball"}

my_dict = { "name" : "Jessica", 1 : [2, 4, 3]}

my_dict = {"name" : "Jessica", "age" : 20}

print(my_dict.get("name"))
print(my_dict["age"])

my_dict["age"] = 21

my_dict["name"] = "Mina"

print(my_dict["name"])
print(my_dict["age"])

my_dict["address"]  = "America"

print(my_dict)

my_dict.pop("age")
print(my_dict)

my_dict.clear()

print(my_dict)