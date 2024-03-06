import os
def listtofile(path,list):
    with open(path,"w") as file:
        for item in list:
            file.write(str(item)+' ')
filepath = "pashamatb.txt"
list = ["tryhard","dontgiveup",123]
listtofile(filepath,list)
