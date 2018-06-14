numbers = [1,2,3]
file = open("numbers.txt", 'w')
for n in numbers:
    file.write(str(n) + '\n')
file.close()