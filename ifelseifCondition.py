def string_length(string):
    if(type(string)==int):
        return("Don't enter an integer")
    elif (type(string)==float):
        return("Don't enter an float")
    else:
       return len(string)
       
print(string_length(110.3))
