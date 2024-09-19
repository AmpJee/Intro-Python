empty_list = []
empty_list = list()
my_list = [1, 2, "ALICE", True]
print(len(my_list))
print(my_list[3:0:-2])
print(my_list[::-1])
my_list.append(4)
print(my_list)
my_list.insert(2, 55)
print(my_list)
my_list.extend([2, 5, 9, 33])
print(my_list)
my_list += [2, 4, 7, 5, 47]
print(my_list)
my_list.pop()
print(my_list)
my_list.pop(5)
print(my_list)
my_list.remove(5)
print(my_list)

count_of_one = my_list.count(2)

for i in range(count_of_one):
    my_list.remove(2)
print(my_list)

