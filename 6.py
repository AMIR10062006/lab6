import os
import string
alphabet = list(string.ascii_uppercase)
for i in alphabet:
    file = open(i+".txt","x")
    file.close()
