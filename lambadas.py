,,def square(num):
    return num**2
my_nums = [1,2,3,4,5]

for item in map(square, my_nums):
    print(item)


allSquares = list(map(square, my_nums)) #goes through my_nums applying the square function and storing it in a list


def splicer(myString):
    if len(myString)%2 == 0:
        return 'EVEN'
    else:
        return myString[0]

names = ['Andy', 'Eve', 'Sally']

results = list(map(splicer, names))


def check_even(num):
    return num%2==0

myNums = [1,2,3,4,5,6,7,8]

filter(check_even, myNums) #filtes base off function, returns a list


def square(num):
    result = num ** 2
    return result

#----------Lambda----------
# functionality to only use once

lambda num: num ** 2

#you can use it in conjunction with maps or filter

list(filter(lambda num: num%2 == 0, myNums)) #3 lines into one