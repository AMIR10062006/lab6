import os
if __name__ == "__main__":
    with open("pashamatb.txt","r",encoding="utf8") as file:
        listoflines = sum(1 for line in file)
    print(listoflines)
