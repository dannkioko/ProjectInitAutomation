import os
import sys
from github import  Github
from dot_env import dot_env

user = os.getenv("USERNAME")
password = os.getenv("PASSwORD")
path = os.getenv("FILEPATH")

def create():
    folderName = str(sys.argv[2])
    projectType = str(sys.argv[1])
    user = Github(username, password).get_user()
    repo = user.create_repo(folderName)