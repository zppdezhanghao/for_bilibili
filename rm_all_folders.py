import os,shutil
for i in os.listdir():
    if not "." in i:
        shutil.rmtree(i)
