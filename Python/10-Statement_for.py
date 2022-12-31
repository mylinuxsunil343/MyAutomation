mylist = [1,2,3,4,5,6,7,8,9]
for num in mylist:
    print(num)

fruits = ["apple","orange","banana"]
for x in fruits:
    if x == 'banana':
        break
    print(x)

mystring = 'Test Tost'
for let in mystring:
    print(let)

for _ in 'Test':
    print('Tost')
# print Marella 5 times which is 5 char in Sunil

tup = (1,2,3)
for item in tup:
    print(item)

mylist = [(1,2),3,(4,5,6)]
for items in mylist:
    print(items)


#tuples unpacking
mynewlist = [(1,2),(3,4),(5,6)]
for a,b in mynewlist:
    print(a) #prints all first values
    print(b) # print all 2nd values

mynewlists = [(1,2,3),(4,5,6),(7,8,9)]
for a,b,c in mynewlists:
    print(a) #prints all first values
    print(b) # print all 2nd values
    print(c)

d = {'k1':1,'k2':2,'k3':3}
for items in d.items():
    print(items)

for key,values in d.items():
    print(key)
    print(values)

for num in range(3,10):
    print(num)

index_count = 0

for letter in 'abcdef':
    print(f'At index {index_count} the letter is {letter}')
    index_count += 1

for item in enumerate('abcdef'):
    print(item)

mylist1 = [1,2,3]
mylist2 = ['a','b','c']
for item1 in zip(mylist1,mylist2):
    print(item1)