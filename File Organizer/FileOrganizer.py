
import os,pathlib,shutil as sh
from datetime import datetime
from xmlrpc.client import DateTime


def move():
    while True:
        print("\n")
        print("current: "+os.getcwd()+"\n")
        print([name for name in os.listdir() if not os.path.isfile(name)])
        print("Chose path (0=quit/1=default)")
        path=input()
        try:
            if(path==".."):
                os.chdir(path)
                continue
            if(path=="0"):
                break
            if(path=="1"):
                os.chdir(defau)
            os.chdir(path)
        except:
            print("error")
            
def copy():
     print("current: "+os.getcwd()+"\n") 
     print([name for name in os.listdir() if not os.path.isfile(name)]) 
     print("Chose folder (0=quit/1=default)")
     path=input()
     try:
         if(path=="0"):
            return
         print("input des name: ") 
         desname=input()
         os.mkdir(os.getcwd()+"\\"+desname)
         count=1
         for name in os.listdir(path):
             if os.path.isfile(path+"\\"+name):
                 add=name.split(".")[0]
                 ext="."+name.split(".")[1]
                 sh.copy(path+"/"+name,os.getcwd()+"\\"+desname+"/"+str(count)+ext)
                 count+=1
         print("Complete")        
     except:
         print("error")
         
def newfoder():
     print("current: "+os.getcwd()+"\n") 
     print("input folder name: ") 
     desname=input()
     os.mkdir(os.getcwd()+"\\"+desname)

def delete():
    print("current: "+os.getcwd()+"\n") 
    print([name for name in os.listdir() if not os.path.isfile(name)]) 
    print("Chose folder to delete")
    desname=input()
    sh.rmtree(os.getcwd()+"\\"+desname)
def menu():
    global defau
    defau=os.getcwd()
    while True:
        os.system('cls')
        print("File Organize\n\
1.Move       \n\
2.Copy       \n\
3.New folder here \n\
4.Delete\n\
5.Show file\n\
0.Quit\n\
Current:"+os.getcwd())
        mode=input()
        match int(mode):
            case 1:
                move()
            case 2:
                copy()
            case 3:
                newfoder()
            case 4:
                delete()
            case 5:
                print([name for name in os.listdir()])
                input()
            case 0:
                break
            case _:
                print("error")

menu()                