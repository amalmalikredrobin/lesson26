

# [1, 2. True, 'Bye']

# a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# b = []
# for num in a:
# a = ['a', 'b', 'c', 'd']
# b = []

# for i in range(len(a) - 1, -1, -1):
#     b.append(a[i])
# print(b)

# a = ['a', 'b', 'c', 'd']
# num = []
# l = []

# for i in range(len(a)):
#     num.append(i * a[i])

# print(num)

# a = ['a', 'b', 'c', 'd']
# b = []

# for i, letter in enumerate(a, 1):
#     b.append(letter * i)
# print(b)

a = ['a', 'b', 'c', 'd']
b = []
for  i, ltr in enumerate(a):
    if i % 2:
        b.append(ltr.upper())
    else:
        b.append(ltr.lower())
print(b)
