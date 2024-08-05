l = [20, 30, 40, 50]
# Delete operator

# del and pop() both are used in delete operation but the difference is del() is not give you any statement that which one is delete but the pop() is give the which one is deleted 

#del
# del l[1] 
# print(l)

# pop()
# l.pop(1)
# print(l)

# remove()
# l.remove(20)
# print(l)

#clear()
# l.clear()
# print(l)

# Updating elements in the list 
 
m = [10, 20, 30, 40, 60]
n = [80, 90]

# m[4] = 50
# print(m) 

# insert( )
# m.insert(4, 50)
# print(m)

# append()
# m.append(n)
# print(m)
# m.append("Hello")
# print(m)

# extend()
m.extend(n)
print(m)