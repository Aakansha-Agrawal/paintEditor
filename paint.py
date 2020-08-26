from tkinter import *
from tkinter import colorchooser
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image
import os

trace = 0
wid = 1700
hgt = 800
clr = "black"
brs_siz = 3
lastx,lasty = 0,0
bg = "white"
fname = "no file"

#message box calling
def msg():
    ans = os.getcwd()
    if (ans != None):
       mbox = messagebox.askyesnocancel("Exit","Do You Want To Save Changes")
       if(mbox == True):
            saveas()
       elif(mbox == False):
           box = messagebox.askyesno("Exit","Do you Want to Open Editor")
           if(box == True):
               tk.destroy()
               import Editor
           else:
               quit()

#create new file
def newfile():
    ans = os.getcwd()
    if (ans != None):
       mbox = messagebox.askyesno("Exit","Do You Want To Save Changes")
       if(mbox == True):
            saveas()
       else:
           tk.destroy()
           import paint

#open file    
#def openfile(self):
 #   self.filename = filedialog.askopenfile(initialdir = os.getcwd(),title = "select file to open",filetypes = [("Paint Images",".png"),("All Images","*.*")])
    #if(r != None):
     #   w.delete()
  #  load = Image.open(self.filename,"r")
   # render = ImageTk.PhotoImage(load)
#    img = Label(self,image=render)
#    img.image = render
#    img.place(x=0, y=0)
#   widt, hght = load
#    w = Canvas(tk, width=widt, height=hght)
#    w.create_image((w / 2, h / 2), image=tkimage)
#    w.pack()
#    fname = r.name
#    r.close()
#    tk.title(os.path.basename(fname) + " - Notepad")

#imgSize = Image.open("ap41,ddr,rrf,sdat,bmp,png") # The only file the loads
#tkimage = ImageTk.PhotoImage(imgSize)
#widt, hght = imgSize.size

#saveas file
def saveas():
    f = filedialog.asksaveasfile(initialfile = 'Untitled.png',mode="w",defaultextension=".png")
    if f is None:
        return
    savetxt = os.getcwd()
    fname = f.name
    f.write(savetxt)
    f.close()
    tk.title(os.path.basename(fname) + " - Paint")

#movement initialize
def paint(event):
    global lastx,lasty
    lastx = event.x 
    lasty = event.y 

#pencil motion initialise    
def on_drag(event):
    brs_siz = scal.get()
    w.create_line(lastx,lasty,event.x,event.y,fill=clr,width=brs_siz,capstyle=ROUND,smooth=TRUE)
    paint(event)

#pencil motion 
def pencilTool():
    w.config(cursor = "pencil")
    w.bind("<ButtonPress-1>",paint)
    w.bind("<B1-Motion>",on_drag)

#spring motion initialise    
def spring(self):
    global brs_siz
    global clr
    global scal
    global x1,x2,y1,y2
    x1,x2,y1,y2 = 0,0,0,0
    brs_siz = scal.get()
    x1 = self.x - brs_siz
    x2 = self.x + brs_siz
    y1 = self.y - brs_siz
    y2 = self.y + brs_siz
    w.create_oval(x1,y1,x2,y2,outline=clr)

#spring motion
def springTool():
    w.config(cursor="crosshair")
    w.bind("<B1-Motion>",spring)

#choose color
def color(clrs):
    global clr
    clrs = colorchooser.askcolor()
    clr = clrs[1]

#color motion
def colorTool():
    w.config(cursor = "spraycan")
    w.bind("<B1-Motion>",color("clr"))
    
#work on eraser        
def erase(event):
    global lastx,lasty
    brs_siz = scal.get()
    w.create_line(lastx,lasty,event.x,event.y,fill="white",width=brs_siz,capstyle=ROUND,smooth=TRUE)
    paint(event)

#eraser motion
def eraserTool():
    w.config(cursor = "dotbox")
    w.bind("<B1-Motion>",erase) 

#clear motion
def clearTool():
    w.bind("<B1-Motion>",w.delete("all"))
    w.bind("<Button-Release>",)


#cirlce class
class CircleDemo: 
    def __init__(self, parent=None):
        w.config(cursor="circle")
        w.bind('<ButtonPress-1>', self.ovl)   
        w.bind('<B1-Motion>',self.on_ovl)          
        self.w = w
        self.drawn  = None
        
    def ovl(self, event):
        self.start = event
        self.drawn = None
        
    def on_ovl(self, event):
        brs_siz = scal.get()
        w = event.widget
        if self.drawn: w.delete(self.drawn)
        objectId = self.w.create_oval(self.start.x, self.start.y, event.x, event.y,outline=clr,width=brs_siz)
        if trace: print (objectId)
        self.drawn = objectId

#square class
class SquareDemo: 
    def __init__(self, parent=None):
        w.config(cursor="crosshair")
        w.bind('<ButtonPress-1>', self.sqr)   
        w.bind('<B1-Motion>',   self.on_sqr)          
        self.w = w
        self.drawn  = None
        
    def sqr(self, event):
        self.start = event
        self.drawn = None
        
    def on_sqr(self, event):
        brs_siz = scal.get()
        w = event.widget
        if self.drawn: w.delete(self.drawn)
        objectId = self.w.create_rectangle(self.start.x, self.start.y, event.x, event.y,outline=clr,width=brs_siz)
        if trace: print (objectId)
        self.drawn = objectId

#rectangle class
class RecDemo: 
    def __init__(self, parent=None):
        w.config(cursor="crosshair")
        w.bind('<ButtonPress-1>', self.rec)   
        w.bind('<B1-Motion>',     self.on_rec)          
        self.w = w
        self.drawn  = None
        
    def rec(self, event):
        self.start = event
        self.drawn = None
        
    def on_rec(self, event):
        brs_siz = scal.get()
        w = event.widget
        if self.drawn: w.delete(self.drawn)
        objectId = self.w.create_rectangle(self.start.x, self.start.y, event.x, event.y,outline=clr,width=brs_siz)
        if trace: print (objectId)
        self.drawn = objectId

#Layout    
tk = Tk()
tk.title("Untitled - Paint")
tk.iconbitmap(r'paint_W2b_icon.ico')
tk.geometry("600x500")

w = Canvas(height=hgt,width=wid,bg = "white")
#frm = Frame(tk,bg = "skyblue")

nbt = PhotoImage(file="add-file.png")
new_btn = Button(image = nbt,command = newfile)
new_btn.grid(row=1,column=0,sticky=S)
#new_btn.place(x=50,y=10)

#opn = PhotoImage(file="untitled.png")
#opn_btn = Button(image = opn,command = lambda:openfile("self"))
#opn_btn.grid(row=1,column=1,sticky=S)
#opn_btn.place(x=150,y=10)

sav = PhotoImage(file="save.png")
sav_btn = Button(image = sav,command = saveas)
sav_btn.grid(row=1,column=1
             ,sticky=S)
#sav_btn.place(row=1,column=1)

pen = PhotoImage(file="pen.png")
brs_btn = Button(image = pen,command = pencilTool)
brs_btn.grid(row=1,column=2,sticky=S)
#brs_btn.place(x=350,y=10)

col = PhotoImage(file="color.png")
colr_btn = Button(image = col,command = colorTool)
colr_btn.grid(row=1,column=3,sticky=S)
#colr_btn.place(x=450,y=10)

ers = PhotoImage(file="eraser.png")
ers_btn = Button(image = ers,command = eraserTool)
ers_btn.grid(row=1,column=4,sticky=S)
#ers_btn.place(x=550,y=10)

sqr = PhotoImage(file="square.png")
sqr_btn = Button(image = sqr,command = SquareDemo)
sqr_btn.grid(row=1,column=5,sticky=S)
#sqr_btn.place(x=650,y=10)

spr = PhotoImage(file="spring.png")
spr_btn = Button(image=spr,command = springTool)
spr_btn.grid(row=1,column=6,sticky=S)
#spr_btn.place(x=750,y=10)

cir = PhotoImage(file="circle.png")
cir_btn = Button(image = cir,command = CircleDemo)
cir_btn.grid(row=1,column=7,sticky=S)
#cir_btn.place(x=850,y=10)

rec = PhotoImage(file="rec.png")
rec_btn = Button(image = rec,command = RecDemo)
rec_btn.grid(row=1,column=8,sticky=S)
#rec_btn.place(x=950,y=10)

scal = Scale(from_ = 1,to = 40,orient = HORIZONTAL,width=10,length=200)
scal.set(3)
scal.grid(row=1,column=9,sticky=S)
#scal.place(x=1050,y=10)

clear = PhotoImage(file="clear.png")
clr_btn = Button(image = clear,command = clearTool)
clr_btn.grid(row=1,column=10,sticky=S)
#clr_btn.place(x=1300,y=10)

ext = PhotoImage(file="ext.png")
ext_btn = Button(image = ext,command = msg)
ext_btn.grid(row=1,column=11,sticky=S)
#ext_btn.place(x=1400,y=10)

tk.protocol("WM_DELETE_WINDOW",msg)

#frm.pack(fill=X)
w.grid(row=2,columnspan=20,pady=40,sticky=S)
#scroll bars
#scrollv = Scrollbar(tk)
#scrollv.pack(side=RIGHT,fill=Y)
#scrollh = Scrollbar(tk, orient=HORIZONTAL)
#scrollh.pack(side=BOTTOM,fill=X)



#yscrollcommand=scrollv.set,xscrollcommand=scrollh.set)#,wrap=NONE)
#scrollv.config(command=w.yview)
#scrollh.config(command=w.xview)
#sticky=allows direction east west north south



