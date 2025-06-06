name ="Jessica"
age = 12
is_student = True
weight = 20.0

print("your name is ", name)
print("Data type of name is", type(name))
print("your age is", age)
print("Data type of age is", type(age))
print("is student", is_student)
print("is_student data type is", type(is_student))
print("your weight is", weight)
print("Data type of weight is", type(weight))

# After type casting
print("After type casting")
age = str(age)
print("Data type of age is", type(age))
weight = str(weight)
print("Data type of weight is", type(weight))