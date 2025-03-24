def write():
    fi=open("test.txt","w")
    i=input("New add ")
    fi.write(i)
    fi.close()
    
def read():
    fi=open("test.txt","r")
    print(fi.read())
    fi.close()
    
def app():
    fi=open("test.txt","a")
    i=input("New add ")
    fi.write(i)
    fi.close()
    
def readl():
    fi=open("test.txt","r")
    print(fi.readline())
    fi.close()
    fi=open("test.txt","r")
    print(fi.readlines())
    fi.close()
   
readl()
