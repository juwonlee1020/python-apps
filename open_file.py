fruit_file = open("fruits.txt")
fruit_content = fruit_file.readlines()
fruit_file.close()
fruit_content = [line.strip() for line in fruit_content]
for f in fruit_content:
    print(len(f))

