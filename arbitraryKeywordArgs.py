def myfunc(a, b): 
    #reurns 5% of the sum of a and b 
    return sum((a, b)) *0.05 
print(myfunc(40, 60))  

def myfunc(*args): #takes an inumerable amount of parameters and uses it as a tuple
    return sum(args)* 0.05

    #returns as a dictionary
def myfunc(**kwargs): #by convention use that keyword yet any name as long as it has two ** at front
    if 'fruit' in kwargs:
        print('found it {}'.format(kwargs['fruit']))
    else:    
        print('nope')
    
myDic = {'fruit':'apple', 'veggie': 'lettuce'}

myfunc(fruit = 'apple')