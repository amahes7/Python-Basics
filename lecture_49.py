def ctf(celsius):
    F=(celsius*9/5)+32
    return F
temperatures = [10, -20, 100]
for i in temperatures :
    print(ctf(i))
