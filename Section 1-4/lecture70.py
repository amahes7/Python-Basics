from datetime import datetime

with open(datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f")+".txt","w") as myfile:
    for i in range(1,4):
        with open("file"+str(i)+".txt","r") as f:
            myfile.write(f.read()+ "\n")

    

