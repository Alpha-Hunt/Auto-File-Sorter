from os import walk
import os
import shutil
import datetime
mypath="C:\\Users\\godla\\Documents\\Completed Projects\\SortX\\Sample files"
destination="C:\\Users\\godla\\Documents\\Completed Projects\\SortX\\Sample files"
f = []
for (dirpath, dirnames, filenames) in walk(mypath):
    f.extend(filenames)
    break
print(f)
n=0

def dirx(source,x,destination,mypath,s):
    Current_Date = datetime.datetime.today().strftime ('%d-%b-%Y')
    editdest=destination+'\\'+x+' files'
    try:
        os.mkdir(editdest)
    except Exception as exc:
        print("folder exists",exc)
    try:
        shutil.move(source, editdest)
    except Exception as moveerr:
        newnamepath=mypath+"\\"+s+str(Current_Date) + str(x)
        os.rename(source,newnamepath)
        shutil.move(newnamepath, editdest)
for allfiles in f:
    print(n)#count
    s,x=os.path.splitext(f[n])
    print(x)#extention
    source=mypath+"\\"+f[n]
    dirx(source,x,destination,mypath,s)
    n+=1
