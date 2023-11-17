# file = open('text.txt', 'r')
# print(file.read(2))
# print(file.read())
# file.close()

with open('text.txt', 'r') as file:
    lines = file.readlines()
    print(lines)

print('file closed')