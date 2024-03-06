import os
def checkpath(path):
    if os.path.exists(path):
        print(f"path {path} exist!")
        print(os.listdir(path))
    else:
        print(f"path {path} doesnot exist(")
        return 0
if __name__ == "__main__":
    path =  input("input path: ")
    checkpath(path)