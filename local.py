import os

def initcommit(path, username, folderName):
    print("******************* Creating Local Directory ("+path+")*******************")
    os.system('mkdir '+path)
    os.system('cd '+path +'&& echo "# '+folderName+'" >> README.md && git init && git add README.md && git commit -m "Initial commit" && git remote add origin https://github.com/'+username+'/'+folderName+'.git'+' && git push -u origin master')
