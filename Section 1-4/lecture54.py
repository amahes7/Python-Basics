numbers = [1,2,3]
newFile = open("numbers.txt","w")
for i in numbers:
    newFile.write(str(i)+"\n")
newFile.close()
