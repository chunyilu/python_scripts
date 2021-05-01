def find_aeiou(input):
    vowel_list = ['a', 'e', 'i', 'o', 'u']
    output = []
    for y in input:
        print('y =' + str(y))
        for x in range(len(vowel_list)):
            if y == vowel_list[x]:
                output.append(y)
    return output

print(find_aeiou('hello world'))