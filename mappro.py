#mapping

nums=[1,2,3,4,5,6]
print(list(map(lambda x:x*2,nums)))
#filter(mapping)
nums=[2,3,5,4,8,9,10]
print(list(filter(lambda x:x%2!=0,nums)))

#reduce list into single element
from functools import reduce
l=[1,2,3,4,5]
print(reduce(lambda x,y:x+y,l))
