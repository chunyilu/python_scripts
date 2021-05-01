x = 2
space_num = 10
for i in range(1, 11):
    #print space
    for k in range(1, space_num):
        print(' ', end=" ")
    #print star
    for j in range(1, x):
        print('*', end=" ")
    print()
    x = x + 2
    space_num = space_num - 1