num_list = []

for i in range(200001):
    serial_num = 'A' + str(i).rjust(6, '0')
    # print(serial_num)
    num_list.append(serial_num)

print(num_list)

for file_index in range(20):
    with open('output_' + str(file_index) + '.csv', 'a', newline='') as csvfile:
        # writer = csv.writer(csvfile)
        for i in range(file_index*10000, file_index*10000+10000):
            csvfile.write(num_list[i])
            csvfile.write('\n')
