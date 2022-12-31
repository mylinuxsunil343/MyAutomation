mylist = [1,2,3,4,5]
print('range function')
for num in range(3,10):
    print(num)
print('Step function in range - multiple of 2')
for num in range(0,11,2):
    print(num)
print('list range - multiple of 2')
print(list(range(0,11,2)))
print('enumerate')
index_count = 0
for letter in 'abcde':
    print('at index {} the letter is {}'.format(index_count,letter))
    index_count += 1

word = 'abcde'
for item in enumerate(word):
    print(item)
