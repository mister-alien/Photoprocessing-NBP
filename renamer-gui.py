import renamethings
from renamethings import renstuff
from appJar import gui
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import askdirectory

def press(btn):
    if(btn=="Cancel"):
        app.stop()
    elif(btn=="Browse"):
        Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
        filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
        app.setEntry("linefile",filename)
    elif(btn=="Rename"):
        renstuff(app.getEntry("linefile"),app.getEntry("workdir"),namecol,platecol,txcol,prefix,offset)
        print("Done")    
    elif(btn=="work dir"):
        Tk().withdraw()
        direct=askdirectory()
        app.setEntry("workdir",direct)
def menuPress(menus):
    if(menus=="Config"):
        print("Dont do it")
    elif(menus=="Info"):
        info=gui()
        info.addLabel("title","Test",0,0,2)
        info.go()
    elif(menus=="Close"):
        app.stop()
        #### Default value block
offset = 2
prefix='IMG_0000'
namecol='A'
txcol='L'
platecol='M'

app=gui()

### fillings

app.addLabel("title","Renamer thing",0,0,2)
#row 0, col 0, span of 2

app.addLabel("linefile","Spreadsheet Path",1,0)
app.addEntry("linefile",1,1)
app.addButton("Browse",press,1,2)

app.addLabel("workdir","Line Folder: ",2,0)
app.addEntry("workdir",2,1)
app.addButton("work dir",press,2,2)

app.addButtons(["Rename","Cancel"],press,3,0,2)

fileMenus = ["Config", "Info","-", "Close"]
app.addMenuList("File",fileMenus,menuPress)

app.setEntryFocus("linefile")

app.go()
