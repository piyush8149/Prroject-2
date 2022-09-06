#Basic string operations

str = "Hello world this is a string!"

print(len(str)) #Get the length
print(str * 3) #Repeat
print(str.replace('Hello','Hola')) #Replace
print(str.split('.')) #split
print(str.startswith('H')) #Start with
print(str.endswith('H')) #Ends with 
print(str.upper())
print(str.lower())
print(str.capitalize())

#slicing = or getting a sub string
print(str[0:5]) #Get the first 5 -zero based
print(str[6:]) #Get the first 6th to the end
print(str[-7:]) #Get the last 7
print(str[6:11]) #Get the first 6 to 11

