
import os
from PyQt6.QtWidgets import QApplication
from PIL import Image 
class t:
    types=""
    bools=0
    def __init__(self,types,bools) -> None:
        self.types=types
        self.bools=bools

class ConvertJPG:
    succeed=[]
    def __init__(self,commendlist : list) -> None:
        self.__com = commendlist
       
        self.where=""
        self.drop =""
        self.file = ""
    def doConvert(self,file,where,drop,print):
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
                self.succeed.append("Save Files! : " +str(new_file))
        except:
            print("Error File :",file)
    def checkCommendOutError(self,commendlist : list)->t:
        w=0
        d=0
        f=0
        for x in commendlist:
            if(x=="-w"):
                w+=1
                self.where = commendlist[commendlist.index(x)+1]
            if(x=="-d"):
                d+=1
            if(x=="-f"):
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

    def commendDo(self,commend : list)->None:
        
        NotFrist = commend[1:]
        for x in NotFrist:
            match x:
                case "-w":
                    self.where=os.path.join(NotFrist[NotFrist.index("-w")+1])
                case "-d":
                    self.drop=os.path.join(NotFrist[NotFrist.index("-d")+1])
                case "-f":
                    self.file=os.path.join(NotFrist[NotFrist.index("-f")+1])
        
    def getcom(self):
        return self.__com
    def DoneCommand(self,types : str,print):
        if types=="wd":
            if(self.drop==""):
                self.drop=self.where
            for file in os.listdir(self.where):
                self.doConvert(file,self.where,self.drop,print)
                
        if  types =="fd":
            if self.drop =="":
                self.drop=self.file
            self.doConvert(self.file,self.where,self.drop,print)

