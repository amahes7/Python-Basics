fruits_file = open("fruits.txt")
content= fruits_file.read()
content=content.splitlines()
for word in content:
    print(len(word))