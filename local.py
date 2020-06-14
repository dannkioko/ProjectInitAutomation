import os

def initcommit(path):
    print("******************* Creating Local Directory ("+path+")*******************")
    os.system('mkdir '+path)
    os.system('cd '+path)
    os.system('git init')
    os.system('git add .')
    os.system('git commit -m "Initial commit"')
