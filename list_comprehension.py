mystring = 'hello'

mylist = []

# for letter in mystring:
#     mylist.append(letter)

# print(mylist)

#same thing
#mylist = [letter for letter in mystring]
    #takes element in my string and appends it

#mylist = [num for num in range(0,11)] #appends 0 to 11
         #^ you can even set oppatratiosn to this num


# mylist = [num**2 for num in range(0,11)] #appends 0 to 11 BUT performs operations to num
# print(mylist)


mylist = [num**2 for num in range(0,11) if num%2==0] #appends 0 to 11
print(mylist)                           #^this acts as the inner part of the loop
#you can even perfom nested loops


