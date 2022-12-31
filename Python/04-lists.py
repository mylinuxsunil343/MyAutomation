mylists = [34,"Sunil",23.2, "Test1", "Test2", "Test3"]
print("My lists 1st - ",mylists[0])
print("My lists 1st - ",mylists[1])
print("My lists 1st - ",mylists[1:])
print("My lists 1st - ",mylists[:1])

new_lists = ["Test2", 32]
print("Concatinated list : ",mylists+new_lists)

mylists[1] = "Test3"
print(mylists)

mylists.append("Test4")
print("My appended lists 1st - ",mylists)

mylists.pop()
print("New lists after pop",mylists)

# you can assign pop value - last value to new variable
pop_list=mylists.pop()
print("Popped value : ",pop_list)

mynumlists = [145,12,42,3,45]
mynumlists.sort()
mynumlist=mynumlists
print(mynumlist)