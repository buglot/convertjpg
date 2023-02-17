from do import ConvertJPG
from convertGUI1 import ConvertGUI

from PyQt6.QtWidgets import QApplication
import sys
import os
if __name__ == "__main__":
    commend = sys.argv
    help="""-help to using
        Commend []:
            [NONE] Auto run -gui
            -w [Folder want convert jpg]
            -d [Folder want to Save]
            -f [One file want convert jpg]
            -gui run Gui 
            Function -gui []: 
                -w [Folder want convert jpg] Auto open folder"""
    
    if(len(commend)==1):
        print(help)
        os.system(f'{commend[0]} -gui')
    else:
        if commend[1] == "-help":
            print(help)
        a = ConvertJPG(commend)
        td =a.checkCommendOutError(a.getcom())
        if commend[1] == "-gui":
            App=QApplication(sys.argv)
            Convert= ConvertGUI("Convert GUI",a)
            Convert.show()
            sys.exit(App.exec())
        
        elif(td.bools):
            a.commendDo(a.getcom())
            a.DoneCommand(td.types,print)
        else:
            print("-help to useing #type",td.types)
            input()