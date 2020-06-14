import os

def initcommit(path, folderName):
    print("******************* Creating Local Directory ("+path+")*******************")
    os.system('cd '+path)
    os.system('mkdir '+folderName)
    os.system('cd '+path+'\\'+folderName)
    os.system('git init')
    os.system('git add .')
    os.system('git commit -m "Initial commit"')
