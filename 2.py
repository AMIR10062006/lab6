import os
def checkpath(path):
    if os.path.exists(path):
        print(f"path {path} exist!")
    else:
        print(f"path {path} doesnot exist(")
    if os.access(path,os.R_OK):
        print(f"path {path} is readable!")
    if os.access(path,os.W_OK):
        print(f"path {path} is writable!")
    if os.access(path,os.X_OK):
        print(f"path {path} is executable!")
        
if __name__ == "__main__":
    dir = input("write ur path: ")
    checkpath(dir)