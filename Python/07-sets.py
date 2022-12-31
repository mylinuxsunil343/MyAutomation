myset = set()
myset.add(1)
print(myset)
myset.add(2)
print(myset)

myset.add(1)
print(myset)
#It will mot add 1 again as sets will consider only uniquw value 

mylist = [1,1,1,3,3,3,2,2,2,7,7,7,4,4,4]
mylist = set(mylist)
print(mylist)

#unorder collections of unique reference