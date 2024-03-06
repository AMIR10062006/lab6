import os
import string
alphabet = list(string.ascii_uppercase)
for i in alphabet:
    os.remove(i+".txt")