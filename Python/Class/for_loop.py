my_list = ['apple', 'bannana', 'cherry','date', 'elderberry','fig', 'gundam']
abc = ['a ','b ','c ','d ','e ','f ','g ']

# count=0
# while count<len(my_list):
#     print(my_list[count])
#     count += 1

for i, j in zip(abc, my_list):
    print(i+'is for ' + j)