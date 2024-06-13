#inbuilt functions
# print(),input, type(), format(), max, min, id(), sum(), avg().....etc

#string functions
name = "Bharathi"
print(name)
print(type(name))
print(id(name)) #id - memory address where it is stored
print(len(name)) #length always starts with 1

name = name.upper() #converts to uppercase
print(name)
name = name.lower() #converts to lowercase
print(name)


a = name.count('h')
print(a)
print(name[7])
#print(name[9]) # string index out of range

# Python is Immutable which means that memory once allocated to something that cannot be changed
name[0] = "P" # 'str' object does not support item assignment