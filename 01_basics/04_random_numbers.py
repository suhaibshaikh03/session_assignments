import random
numbers_list = []
for i in range(10):
    rand_no = random.randint(1,100)
    numbers_list.append(rand_no)
    print(rand_no,end=" ")

print("\nnumbers_list:",numbers_list)