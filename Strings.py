str = "Hello world"
str = str.replace("o", "i")
name = "Carlton V Gracias"
print(name[3])
print(type(name[3]))
print(name[0:7]) #Note: The upper bounds are not included
print(name[-7:])
first_name_idx = name.find(" ")
print(first_name_idx)
first_name = name[:first_name_idx]
second_name_idx = name.find(" ", first_name_idx+1)
second_name = name[second_name_idx +1:]
print("First name is : " + first_name)
print("Second name is: " + second_name)
