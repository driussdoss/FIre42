import os


###!!!!---work with dir---!!!###
#pwd
print(os.getcwd())

#cd
os.chdir("/home/user/devops/")

#mkdir
os.mkdir("folder_name") #for making one folder
os.makedirs("path_to_folder", exist_ok=True) #for making structure of dir

#rm
os.rmdir("data") #work like rm
import shutil
shutil.rmtree("data") #work like rm -rf

#ls
print(os.lstdir("path")) #work like ls


###!!!---work with files---!!!###
#file exist?
os.path.exist("file_name")

#get name or/and file extention
name, ext = os.path.splitext("file_name")
print(name)
print(ext)

#get size
print(os.path.getsize("file_name"), "byte")


###!!!---path and join---!!!###
#path join???
path = os.path.join("path", "file_name")
print(path)

#absolute path
os.path.abspath("file_name")

#path to folder were file exist
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


###!!!---environment variable---!!!###
#get env var
print(os.environ.get("your variable"))

#create you own env var
os.environ["YOUR ENVIRONMENT VARIABLE"] = "something"

###!!!---system commands---!!!##
os.system("you command")

#check your platform
import sys
print(sys.paltform)


###!!!---EXAMPLES---!!!###
#create file and write some text
import os

os.makedirs("logs", exist_ok=True)
path = os.path.join("logs", "app.log")

with open(path, "a") as f:
    f.write("Программа запущена\n")

print("Лог записан в:", path)

#Itarating over files in a dir
import os

for file in os.listdir("."):
    if os.path.isfile(file):
        print("Файл:", file)

#clear tempor dir
import os, shutil

tmp_dir = "tmp"
if os.path.exists(tmp_dir):
    shutil.rmtree(tmp_dir)

os.makedirs(tmp_dir)
print("Папка tmp создана заново")

#creating dataed logs
import os
from datetime import date

folder = os.path.join("logs", str(date.today()))
os.makedirs(folder, exist_ok=True)

with open(os.path.join(folder, "today.log"), "w") as f:
    f.write("Лог за сегодня.")

#check env var
import os

token = os.environ.get("API_TOKEN")
if not token:
    print("⚠️ Не задан токен!")
else:
    print("Токен найден:", token)

