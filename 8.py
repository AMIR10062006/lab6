import os
def checkpath(path):
    if os.path.exists(path):
        print(f"path {path} exist!")
        return True
    else:
        print(f"path {path} doesnot exist(")
        return 0

if __name__ == "__main__":
    dir = input("write ur path: ")
    if checkpath(dir):
        os.remove(dir)

