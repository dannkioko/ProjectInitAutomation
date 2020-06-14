import os
import sys
from dotenv import load_dotenv
from git import Git
from local import initcommit

load_dotenv(override = True)

user = os.getenv("USERNAME")
password = os.getenv("PASSwORD")

instance = Git(user,password)

def create():
    if "-p" in sys.argv:
        path = sys.argv[sys.argv.index('-p')+1]
        name = path.split("\\")[-1]
        print(name)
        initcommit(path, name)
        os.system('git remote add origin https://github.com/'+user+'/'+'')
        instance.login()
        instance.createRepo(path)
    

if __name__ == "__main__":
    print("*********************** Porject Init Script **********************")
    print("\n \n \n \n")
    create()

