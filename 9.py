from functools import reduce
list = [1,2,3,4,6]
product = reduce(lambda a,b:a*b,list)
print(product)