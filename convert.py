import sys
import os
from PIL import Image 
commend = sys.argv
Errors=[]
succeed=[]
class t:
    types=""
    bools=0
    def __init__(self,types,bools) -> None:
        self.types=types
        self.bools=bools
def checkCommendOutError(commendlist : list)->t:
    w=0
    d=0
    f=0
    for x in commendlist:
        
        if(x=="-w"):
            w+=1
        if(d=="-d"):
            d+=1
        if(f=="-f"):
            f+=1
    if w==1 and d == 1:
        return t("wd",True)
    elif f==1 and d== 1:
        return t("fd",True)
    elif w==1 and f==0:
        return t("wd",True)
    elif f==1 and w==0:
        return t("fd",True)
    return t(0,False)
def commendDo(commend : list,types)->None:
    where=""
    drop =""
    file = ""
    t=""
    NotFrist = commend[1:]
    for x in NotFrist:
        match x:
            case "-w":
                where=os.path.join(NotFrist[NotFrist.index("-w")+1])
            case "-d":
                drop=os.path.join(NotFrist[NotFrist.index("-d")+1])
            case "-f":
                file=os.path.join(NotFrist[NotFrist.index("-f")+1])
    if types=="wd":
        if(drop==""):
            drop=where
        for file in os.listdir(where):
            try:
                new_file=""
                abfile = os.path.join(where,file)
                img = Image.open(abfile).convert('RGB')
                namefile = file.split(".")
                for d in namefile[:-1]:
                    new_file+=d
                new_file = new_file+".jpg"
                new_file_dir=os.path.join(drop,new_file)
                img.save(new_file_dir)
                succeed.append("Save Files!!!! : " +str(new_file))
            except:
                print("Error File:",file)
            
    if  types =="fd":
        if drop =="":
            drop=file
        try:
            new_file=""
            img = Image.open(os.path.join(where,file))
            file = file.split(".")
            for d in file[:-1]:
                new_file+=d
            img.save(os.path.join(new_file,file) + ".jpg")
        except: print("Error File:",file)
if(len(commend)==1):
    print("-help to useing")
    input()
else:
    a = checkCommendOutError(commend)
    if(a.bools):
        commendDo(commend,a.types)
    else:
        print("-help to useing")
        input()
print(*succeed ,sep="\n")