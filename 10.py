with open("pashamatb.txt","r") as file:
    counter = file.read()
upper = sum(1 for i in counter if i.isupper())
lower = sum(1 for i in counter if i.islower())
print(f"number of upper - {upper}")
print(f"number of lower - {lower}")