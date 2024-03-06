import os 
with open("pashamatb.txt","r") as file:
    content = file.read()
with open("poligon.txt","w") as file2:
    file2.write(content)