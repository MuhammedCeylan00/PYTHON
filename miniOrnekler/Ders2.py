fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

# range
for i in range(6):
    print(i)  # 0,1,2,3,4,5

for j in range(3, 6):
    print(j)  # 3,4,5

for k in range(3, 8, 2):
    print(k)  # 3,5,7

# iç içe listeler
lists = [[1, 2, 3], [4, 5, 6]]

for list in lists:
    for i in list:
        print(i)
