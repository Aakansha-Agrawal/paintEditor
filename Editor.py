from tkinter import *
from tkinter import messagebox
from tkinter import colorchooser
import wikipedia
from tkinter.filedialog import askopenfile,asksaveasfile
import os

fname = "no file"

#working with font
try:
    from tkinter import Tk
    
except ImportError:
    from Tkinter import Tk  
    from ttk import Style, Button, Label
from sys import platform
from tkfontchooser  import askfont

#font function
def callback():
    # open the font chooser and get the font selected by the user
        font = askfont(tk)
    # font is "" if the user has cancelled
        if font:
        # spaces in the family name need to be escaped
            font['family'] = font['family'].replace(' ', '\ ')
            font_str = "%(family)s %(size)i %(weight)s %(slant)s" % font
        if font['underline']:
            font_str += ' underline'
        if font['overstrike']:
            font_str += ' overstrike'
        label=Label(tk)        
        label.configure(font=font_str, text='Chosen font: ' + font_str.replace('\ ', ' '))

#contact_us window function  
def aboutus():
    abt=Tk()
    abt.title("About Us")
    #ab.geometry("600x500")

    ab = Frame(abt,width=2000,height=800)
    frm1 = Frame(ab)
    frm2 = Frame(ab)
    frm3 = Frame(ab)
    frm4 = Frame(ab)
    frm5 = Frame(ab)
    frm6 = Frame(ab)
    frm7 = Frame(ab)
    frm8 = Frame(ab)
    frm9 = Frame(ab)
     
    l4=Label(frm4,font=("Forte",20),text="Aakansha Agrawal")
    l4.pack()#grid(row=0,column=1)
    l5=Label(frm5,font=(20),text="aakanshaagrawal16@gmail.com")
    l5.pack()#grid(row=2,column=5)
    l6=Label(frm6,font=(20),text="6395042428")
    l6.pack()#grid(row=3,column=5)

    ab.pack()
    frm1.grid(row=0,column=0)
    frm2.grid(row=1,column=0)
    frm3.grid(row=2,column=0)
    frm4.grid(row=0,column=1)
    frm5.grid(row=1,column=1)
    frm6.grid(row=2,column=1)
    frm7.grid(row=0,column=2)
    frm8.grid(row=1,column=2)
    frm9.grid(row=2,column=2)

#help window function
def helpp(): 
    
    win=Toplevel()
    win.title("Help")
    win.geometry("600x500")
    
    #scrollv = Scrollbar(win)
    #scrollv.pack(side=RIGHT,fill=Y)
    he = Frame(win,bg="white",width=2000,height=800)
    #scrollv.config(command=he.yview)
    
    lb1=Label(he,bg="white",text="Editor is a very basic text editor that has been part of Windows for a very long time.")
    lb1.grid(row=0,columnspan=12)
    lb2=Label(he,bg="white",text="It is excellent for writing relatively short text documents that you want to save as plain")
    lb2.grid(row=1,columnspan=12)
    lb3=Label(he,bg="white",text="text and that is not all you can do with it. If you have not used Editor much, you may be ")
    lb3.grid(row=2,columnspan=12)
    lb4=Label(he,bg="white",text="surprised by how easy it is to work with. Let's take a new look at this old desktop app for") 
    lb4.grid(row=3,columnspan=12)
    lb5=Label(he,bg="white",text="Windows, what it is, what it does:")
    lb5.grid(row=4,columnspan=12)
    lb6=Label(he,bg="white",font=("Forte",15),text="#How to open Editor?")
    lb6.grid(row=5,columnspan=12)
    lb7=Label(he,bg="white",text="Before seeing what you can do with Editor, you have to know how to start it. The easiest way") 
    lb7.grid(row=6,columnspan=12)
    lb8=Label(he,bg="white",text="to do that is to search for it. In Windows 10, type editor in the search box on the taskbar and") 
    lb8.grid(row=7,columnspan=12)
    lb9=Label(he,bg="white",text="click or tap on the Editor search result.")
    lb9.grid(row=8,columnspan=12)
    lb10=Label(he,bg="white",text="Let's take a look at what you can do. Everything should be reassuringly familiar, but keep in mind ")
    lb10.grid(row=9,columnspan=12)
    lb11=Label(he,bg="white",text="that Editor is just a text editor. If you try to paste graphics into it, it does not work.")
    lb11.grid(row=10,columnspan=12)
    lb12=Label(he,bg="white",font=("Forte",15),text="1. Create, open and save text files with Editor")
    lb12.grid(row=11,columnspan=12)
    lb13=Label(he,bg="white",text="The choices you have in the File menu are New, Open, Save, Save As")           
    lb13.grid(row=12,columnspan=12)
    lb14=Label(he,bg="white",text="Creating and saving text documents in Editor is simple: open Notepad, start typing and edit the") 
    lb14.grid(row=13,columnspan=12)
    lb15=Label(he,bg="white",text="text and format it as you see fit. Once you are finished, use the Save As command to save your work.") 
    lb15.grid(row=14,columnspan=12)
    lb16=Label(he,bg="white",text="the default folder is the OneDrive folder in Windows 10 and 8.1, and the My Documents folder in Windows7")
    lb16.grid(row=15,columnspan=12)
    lb17=Label(he,bg="white",text="you can change this quite easily: use the Save As command and browse to your preferred folder and click Open.") 
    lb17.grid(row=16,columnspan=12)
    lb18=Label(he,bg="white",text="notepad will remember your choice. Keep in mind that your files are saved with a .txt extension and in plain text")
    lb18.grid(row=17,columnspan=12)
    lb19=Label(he,bg="white",font=("Forte",15),text="2. Save files as HTML files")
    lb19.grid(row=18,columnspan=12)
    lb20=Label(he,bg="white",text="You can also use Editor to create HTML files. Make sure that Word Wrap is turned on (we will discuss this in just a")
    lb20.grid(row=19,columnspan=12)
    lb21=Label(he,bg="white",text="minute) and type your HTML code the way you would type plain text. When it comes time to save your work, choose Save As,")
    lb21.grid(row=20,columnspan=12)
    lb22=Label(he,bg="white",text="and select All Files from the list of choices. Then save your file with the .htm or .html extension.")
    lb22.grid(row=21,columnspan=12)
    lb23=Label(he,bg="white",font=("Forte",15),text="3. Make simple edits to the text")
    lb23.grid(row=22,columnspan=12)
    lb24=Label(he,bg="white",text="The Edit menu offers a few choices, but again, everything on this menu should be familiar to anyone who has used Windows.")
    lb24.grid(row=23,columnspan=12)           
    lb25=Label(he,bg="white",text="All the Edit choices have associated keyboard shortcuts. Note that most of the commands will be greyed out until there is")
    lb25.grid(row=24,columnspan=12)
    lb26=Label(he,bg="white",text="text selected in the Editor window.The first item on the Edit menu is Undo/Redo, which can be useful when you are editing")
    lb26.grid(row=25,columnspan=12)
    lb27=Label(he,bg="white",text="the document. What appears in this place depends on what you have been doing. If you have just used the Undo command or") 
    lb27.grid(row=26,columnspan=12)
    lb28=Label(he,bg="white",text="pressed Ctrl+Z, you should see the Redo command at the top of the list (and its keyboard shortcut, Ctrl+Y). The rest of the")         
    lb28.grid(row=27,columnspan=12)
    lb29=Label(he,bg="white",text="menu, Cut, Copy, Paste, Delete in nearly all Windows programs that deal with documents.")
    lb29.grid(row=28,columnspan=12)
    lb30=Label(he,bg="white",text="Go To is the less familiar command in this list. It is used in conjunction with Word Wrap, which we will discuss in just a")
    lb30.grid(row=29,columnspan=12)           
    lb31=Label(he,bg="white",text="minute. Go To only works if Word Wrap is turned off, and only if your document contains numbered lines. If Word Wrap is on,")
    lb31.grid(row=30,columnspan=12)           
    lb32=Label(he,bg="white",text="Go To is greyed out. You use Go To to jump to a particular numbered line in the document.")
    lb32.grid(row=31,columnspan=12)           
    lb33=Label(he,bg="white",font=("Forte",15),text="4. Change the font of the text")
    lb33.grid(row=32,columnspan=12)           
    lb34=Label(he,bg="white",text="The Font choice is self-explanatory: it offers you a list of all your installed fonts, and the option to use bold, italic, and ")
    lb34.grid(row=33,columnspan=12)           
    lb35=Label(he,bg="white",text="the like. However, unlike the way it works in programs like Microsoft Word, a change of font immediately affects the entire ")
    lb35.grid(row=34,columnspan=12)           
    lb36=Label(he,bg="white",text="document. You cannot use one font in one part of the document and another font in another part of it. It is all or nothing.")
    lb36.grid(row=35,columnspan=12)
    lb37=Label(he,bg="white",text="The Font choice is self-explanatory: it offers you a list of all your installed fonts, and the option to use bold, italic, and ")
    lb37.grid(row=36,columnspan=12)
    lb38=Label(he,bg="white",text="the like. However, unlike the way it works in programs like Microsoft Word, a change of font immediately affects the entire document")
    lb38.grid(row=37,columnspan=12)
    lb39=Label(he,bg="white",text="You cannot use one font in one part of the document and another font in another part of it. It is all or nothing.")
    lb39.grid(row=38,columnspan=12)
    lb40=Label(he,bg="white",text="In the Font menu, there is a less familiar option available, the drop-down menu labeled Script. This lets you choose characters that")
    lb40.grid(row=39,columnspan=12)           
    lb41=Label(he,bg="white",text="are not available in the standard (western) style fonts. The choices are Western, Greek, Turkish, Baltic (not available in Windows 7),")
    lb41.grid(row=40,columnspan=12)
    lb42=Label(he,bg="white",text="Central European, Cyrillic and Vietnamese (not available in Windows 7). Choose a set, and you should see some representative characters")
    lb42.grid(row=41,columnspan=12)
    lb43=Label(he,bg="white",text="above it. The Western set is selected by default, and you need to change it to another one if necessary.")
    lb43.grid(row=42,columnspan=12)
    lb44=Label(he,bg="white",font=("Forte",15),text="5. you can play with PAINT")
    lb44.grid(row=43,columnspan=12)             
    he.pack()

#call paint
def paintapp():
    ans = TextArea.get(1.0,END)
    if (ans != None):
       mbox = messagebox.askyesno("Exit","Do You Want To Save Changes")
       if(mbox == True):
            save()
       else:
        tk.destroy()
        import paint

#create new file
def newfile():
    ans = TextArea.get(1.0,END)
    if (ans != None):
       mbox = messagebox.askyesno("Exit","Do You Want To Save Changes")
       if(mbox == True):
            save()
       else:
           TextArea.delete(1.0,END)
           fname = "Untitled"
           tk.title(os.path.basename(fname) + " - Notepad")

#open file    
def openfile():
    r = askopenfile(initialdir = "/",title = "select file to open",filetypes = (("text files",".txt"),("All Files","*.*")))
    if(r != None):
        TextArea.delete(1.0,END)
        for i in r:
            TextArea.insert(END,i)
    fname = r.name 
    r.close()
    tk.title(os.path.basename(fname) + " - Notepad")

#saveas file
def saveas():
    f = asksaveasfile(initialfile = 'Untitled.txt',mode="w",defaultextension=".txt")
    if f is None:
        return
    savetxt = TextArea.get(1.0,END)
    fname = f.name
    f.write(savetxt)
    f.close()
    tk.title(os.path.basename(fname) + " - Notepad")

#save file
def save():
    if(fname == "no file"):
        saveas()
    else:
        f = open(fname,"w")
        f.write(TextArea.get(1.0,END))
        f.close()
        tk.title(os.path.basename(fname) + " - Notepad")
        
#cut function    
def cut():
    copy()
    TextArea.delete("sel.first","sel.last")

#copy function
def copy():
    TextArea.clipboard_clear()
    TextArea.clipboard_append(TextArea.selection_get())

#paste function
def paste():
    TextArea.insert(INSERT,TextArea.clipboard_get())

#message box function
def msg():
    ans =TextArea.get(1.0,END)
    if (ans != "None"):
        mbox = messagebox.askyesnocancel("Exit","Do You Want To Save Changes")
        print(mbox)
        if(mbox == True):
            saveas()
        elif(mbox == False):
            quit()

#choose color 
def colrr(colour):
    colour = colorchooser.askcolor()
    txt = TextArea.get(1.0,END)
    txt.colour[1.0,END]
    
    
#search function    
def srch():
    value = ent.get()
    TextArea.delete(1.0,END)
    try:
        ans_v = wikipedia.summary(value)
        TextArea.insert(INSERT,ans_v)
    except:
        TextArea.insert(INSERT,"Please Check Your Connection Or Input")

#upload function
def upload(fname):
    s = TextArea.get(1.0)
    for i in s:
        print("line-",i)
        i = i+1
    
#main menus                
tk=Tk()

b=StringVar()
tk.title("Untitled - Editor")
tk.iconbitmap(r'thyflslrct_1RN_icon.ico')
tk.geometry("600x500")

ent = Entry(tk,width=60,bd="5")
btn = Button(tk,text="Search",bd="5",font="Forte",command=srch,width=10,height=0)
btn1 = Button(tk,text="Help",bd="5",font="Forte",width=5,height=0,command=helpp)
btn2 = Button(tk,text="Contact Us",bd="5",font="Forte",width=10,height=0,command=aboutus)
   
TextArea =Text(tk,undo=True)
file=None
TextArea.pack(expand=True,fill=BOTH)

menu=Menu(tk)

filemenu=Menu(menu,font="Forte",tearoff = False)
filemenu.add_command(label="New File",font="Forte",command=newfile)
filemenu.add_command(label="Open... ",font="Forte",command=openfile)
filemenu.add_separator()
filemenu.add_command(label="Save",font="Forte",command=save)
filemenu.add_command(label="Save As ",font="Forte",command=saveas)
filemenu.add_separator()
filemenu.add_command(label="Exit",font="Forte",command=quit)

editmenu=Menu(menu,tearoff = False)
editmenu.add_command(label="Undo",font="Forte",command=TextArea.edit_undo)
editmenu.add_command(label="Redo",font="Forte",command=TextArea.edit_redo)
editmenu.add_separator()
editmenu.add_command(label="Cut ",font="Forte",command=cut)
editmenu.add_command(label="Copy",font="Forte",command=copy)
editmenu.add_command(label="Paste",font="Forte",command=paste)

formatmenu=Menu(menu,tearoff = False)
formatmenu.add_command(label="Font...",font="Forte",command=callback)                      
formatmenu.add_command(label="Color...",font="Forte",command=lambda:colrr("colour"))

viewmenu=Menu(menu,tearoff = False)
viewmenu.add_command(label="Status Bar",font="Forte",command=lambda:upload("fname"))

paintmenu=Menu(menu,tearoff = False)
paintmenu.add_command(label="Open Paint",font="Forte",command=paintapp)

menu.add_cascade(label="File",font="Forte",menu=filemenu)
menu.add_cascade(label="Edit",menu=editmenu)
menu.add_cascade(label="Format",menu=formatmenu)
menu.add_cascade(label="View",menu=viewmenu)    
menu.add_cascade(label="Paint",menu=paintmenu)

tk.config(menu=menu)
tk.protocol("WM_DELETE_WINDOW",msg)

Scroll=Scrollbar(TextArea)
Scroll.pack(side=RIGHT,  fill=Y)
Scroll.config(command=TextArea.yview)
TextArea.config(yscrollcommand=Scroll.set)

#Scrol = Scrollbar(TextArea,orient=HORIZONTAL)    
#Scrol.pack(side=BOTTOM,fill=X)
#Scrol.config(command=TextArea.xview)
#TextArea.config(xscrollcommand=Scrol.set,wrap = N

btn.pack(side=BOTTOM)
ent.pack(side=BOTTOM)
btn1.pack(side=RIGHT)
btn2.pack(side=RIGHT)
TextArea.pack()

#style = Style(tk)
    #if "win" == platform[:3]:
        #style.theme_use('vista')
    #elif "darwin" in platform:
        #style.theme_use('clam')
    #else:
        #style.theme_use('clam')
    #bg = style.lookup("TLabel", "background")
    #tk.configure(bg=bg)
    #label = Label(tk, text='Chosen font: ')
    #label.pack(padx=10, pady=(10,4))
