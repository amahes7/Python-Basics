temperatures = [10,-20,-289,100]
def writer(temp,path):
    with open(path,"w") as myfile:
        for t in temp:
            if(t > -273.15):
                 f = t* 9/5 + 32
                 myfile.write(str(f) +"\n")

writer(temperatures,"lecture_69.txt")