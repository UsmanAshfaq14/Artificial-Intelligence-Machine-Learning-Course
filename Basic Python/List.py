#1. List Comprehensions
a = [2,3,4,5]

res = [val ** 2 for val in a]

print(res) # [4, 9, 16, 25]

#2. List Comprehensions with if condition
a = [2,3,4,5]

res = [val ** 2 for val in a if val % 2 == 0]

print(res) # [4, 16]

#3. List Comprehensions with if else condition
a = [2,3,4,5]
res = [val ** 2 if val % 2 == 0 else val ** 3 for val in a]

print(res) # [4, 27, 16, 125]

#4. List Comprehensions and for loop
a = [2,3,4,5]
res = []
for val in a:
    if val % 2 == 0:
        res.append(val ** 2)
    else:
        res.append(val ** 3)
print(res) # [4, 27, 16, 125]

#5. List Comprehensions and flatening a list
a = [[1,2,3],[4,5,6],[7,8,9]]
res = [val for sublist in a for val in sublist]
print(res) # [1, 2, 3, 4, 5, 6, 7, 8, 9]