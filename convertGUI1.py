from PyQt6.QtWidgets import QWidget,QHBoxLayout,QVBoxLayout,QPushButton,QListWidget,QFileDialog,QLabel
from do import ConvertJPG
import os
class ConvertGUI(QWidget):
    def __init__(self,Title,converts :ConvertJPG):
        super().__init__()
        self.setWindowTitle(Title)
        self.setGeometry(30,30,300,300)
        self.convert = converts

        self.mainLayout = QHBoxLayout()
        self.PanelLayout1 = QVBoxLayout()
        self.PanelLayout2 = QVBoxLayout()
        self.ButtonLayout = QHBoxLayout()
        self.label1 = QLabel("Files")
        self.label2 = QLabel("Consloe")
        self.setLayout(self.mainLayout)
        self.PanelLayout1.addLayout(self.ButtonLayout)

        self.openfolderB = QPushButton("Open folder")
        self.savefolderB = QPushButton("Save folder")
        self.doConB = QPushButton("Convert")

        self.ViwList = QListWidget()
        self.ViwConsloe = QListWidget()
        self.PanelLayout1.addWidget(self.label1)
        self.PanelLayout1.addWidget(self.ViwList)
        self.ButtonLayout.addWidget(self.openfolderB)
        self.ButtonLayout.addWidget(self.savefolderB)
        self.ButtonLayout.addWidget(self.doConB)
        self.doConB.setEnabled(False)
        self.mainLayout.addLayout(self.PanelLayout1)
        self.mainLayout.addLayout(self.PanelLayout2)
        self.PanelLayout2.addWidget(self.label2)
        self.PanelLayout2.addWidget(self.ViwConsloe)
        self.ViwConsloe.setMaximumWidth(400)
        self.ViwList.setMinimumWidth(300)
        self.OPEN = QFileDialog()
        self.ViwList.itemDoubleClicked.connect(self.openfilesClickinViwlist)
        self.openfolderB.clicked.connect(self.opensFolder)
        self.savefolderB.clicked.connect(self.opensSave)
        self.doConB.clicked.connect(self.doConvertB)
        self.ViwConsloe.itemDoubleClicked.connect(self.openfilesClickinViwConsole)

        if self.convert.where!="":
            self.runFileFolder()
            self.doConB.setEnabled(True)

    def opensFolder(self):
        e=""
        e=self.OPEN.getExistingDirectory(self,"Open folder","C:\\" if self.convert.where=="" else self.convert.where,QFileDialog.Option.ShowDirsOnly)
        if e !="":
            e=os.path.realpath(e)
            self.doConB.setEnabled(True)
            self.convert.where=e
            self.runFileFolder()

            print(f"Select forlder:{e}")
           
    def opensSave(self):
        e=""
        e=self.OPEN.getExistingDirectory(self,"Save folder","",QFileDialog.Option.ShowDirsOnly)
        if e !="":
            self.convert.drop=e
            print(f"Save to forlder:{e}")
    def runFileFolder(self):
        self.ViwList.clear()
        for x in os.listdir(self.convert.where):
            s=x.split(".")
            self.ViwList.addItem(f"{s[-1].upper()} : {x}")
    def openfilesClickinViwlist(self,ss):

            a=ss.text().split(" : ")
            textfile = os.path.join(self.convert.where,a[1])
            if os.path.exists(textfile):
                os.system(f'"{textfile}"')
            else:
                self.printsE("Not Found File :",textfile)
    def printsE(self,*a0):
        string=""
        for x in a0:
            string+=x+" "
        self.ViwConsloe.addItem(string)
    def doConvertB(self):
        self.convert.DoneCommand("wd",self.printsE)
        for x in self.convert.succeed:
            self.printsE(f"{x}")
    def openfilesClickinViwConsole(self,ss):
            textfile=""
            a=ss.text().split(" : ")
            if a[0] == "Error File":
                textfile = os.path.join(self.convert.where,a[1])
            elif a[0] == "Save File!":
                textfile = os.path.join(self.convert.where,a[1])
            if textfile!="":    
                if os.path.exists(textfile):
                    os.system(f'"{textfile}"')
            else:
                textfile = os.path.join(self.convert.where,a[1])
                self.printsE("Can't Open :",os.path.join(self.convert.where,textfile))

