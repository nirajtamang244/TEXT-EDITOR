from tkinter import *
from tkinter.ttk import *
from tkinter import font,colorchooser,filedialog,messagebox
import os
import tempfile
from datetime import datetime



#Funtionality Part

def statusBarFunction(event):
        """CREATING STATUS BAR FUNCTION """
    # if textarea.edit_modified():
        words=len(textarea.get(0.0,END).split())
        characters=len(textarea.get(0.0,'end-1c').replace(' ','')) #1.0
        status_bar.config(text=f'Charecters: {characters} Words: {words}')

        textarea.edit_modified(False)#SETTING THE TEXT MODIFICATION TO FALSE UNTIL THE TEXT IS MODIFIED

def printout(event=None):
    """define function prints and prints the file"""
    file=tempfile.mktemp('.txt')
    open(file,'w').write(textarea.get(1.0,END))
    os.startfile(file,'print')

url=''
def new_file(event=None):
    """function to define new file and makes new document"""
    global url
    url=''
    textarea.delete(0.0,END)

def open_file(event=None):
    """function to define open file which opens a preexisting document"""
    global url
    url=filedialog.askopenfilename(initialdir=os.getcwd,title='Select File',filetypes=(('Text File','txt'),('All Files','*.*')))
    if url != '':
        data=open(url,'r')
        textarea.insert(0.0,data.read())
    root.title(os.path.basename(url))

def save_file(event=None):
    """saves the file with the existing name of the document"""
    if url =='':
        save_url=filedialog.asksaveasfile(mode='w',defaultextension='.txt',filetypes=(('Text File','txt'), ('All Files','*.*')))
        if save_url is None:
            pass
        else:
            content=textarea.get(0.0,END)
            save_url.write(content)
            save_url.close()

    else:
        content=textarea.get(0.0,END)
        file=open(url,'w')
        file.write(content)

def saveas_file(event=None):
    """saves the file with the new name for the document"""
    save_url = filedialog.asksaveasfile(mode='w', defaultextension='.txt', filetypes=(('Text File', 'txt'),('All Files', '*.*')))

    content = textarea.get(0.0, END)
    save_url.write(content)
    save_url.close()
    if url !='':
        os.remove(url)


fontSize=12
fontStyle='arial'
def font_style(event):
    """defines a function font style which changes the font style"""
    global fontStyle
    fontStyle=font_family_variable.get()
    textarea.config(font=(fontStyle,fontSize))

def font_size(event):
    """defines  a function font size which changes the font size"""
    global fontSize
    fontSize=size_variable.get()
    textarea.config(font=(fontStyle,fontSize))# changes the font size of the displayed text area

def bold_text():
    """defines a function bold that makes the text bold if normal and bold if normal"""
    text_property=font.Font(font=textarea['font']).actual()
    if text_property['weight']=='normal':#changes the text to bold
        textarea.config(font=(fontStyle,fontSize,'bold'))

    if text_property['weight']=='bold':#changes the text to bold
        textarea.config(font=(fontStyle,fontSize,'normal'))

def italic_text():
    """defines a function itlic text which makes the text italic if normal and vice versa"""
    text_property = font.Font(font=textarea['font']).actual()
    if text_property['slant']=='roman':#changes to italic if roman
        textarea.config(font=(fontStyle,fontSize,'italic'))

    if text_property['slant']=='italic':#changes to roman if italic
        textarea.config(font=(fontStyle,fontSize,'roman'))

def underline_text():
    """defines a function underline text which underlines the text in the document and removes underline if there is underline"""
    text_property = font.Font(font=textarea['font']).actual()
    if text_property['underline']==0:# inserts the underline if not underline
        textarea.config(font=(fontStyle,fontSize,'underline'))

    if text_property['underline']==1:# puts non-underlined text if  underlined
        textarea.config(font=(fontStyle,fontSize,))

def color_select():
    """defines a function color which changes the color of the text"""
    color=colorchooser.askcolor()
    textarea.config(fg=color[1])#changes the colot of the text area

def align_right():
    """defines a function align right which aligns the whole text to the right side of the document"""
    data=textarea.get(0.0,END)
    textarea.tag_config('right',justify=RIGHT)
    textarea.delete(0.0,END)
    textarea.insert(INSERT,data,'right')

def align_left():
    """defines a function align left which aligns the whole text to the left side of the document"""
    data=textarea.get(0.0,END)
    textarea.tag_config('left',justify=LEFT)
    textarea.delete(0.0,END)
    textarea.insert(INSERT,data,'left')

def align_center():
    """defines a function to make the text to the center of the document"""
    data=textarea.get(0.0,END)
    textarea.tag_config('center',justify=CENTER)
    textarea.delete(0.0,END)
    textarea.insert(INSERT,data,'center')


root=Tk()
root.title('Text Editor')#adding the title to the box
root.geometry('1200x620+10+10')#fitting to the screen with x and y coordinates
root.resizable(False,False)#fixing it so that the button wont get disattached
menubar=Menu(root)#creating the object as menubar
root.config(menu=menubar)#CREATING CONFIG menu for menubar


#file menu section
filemenu=Menu(menubar,tearoff=False)
menubar.add_cascade(label='File',menu=filemenu)#adds file to the menubar
filemenu.add_command(label='New',accelerator='Ctrl+N',command=new_file)#creating the label for new file and shortcut key
filemenu.add_command(label='Open',accelerator='Ctrl+O',command=open_file)#creating the label for open file and shortcut key
filemenu.add_command(label='Save',accelerator='Ctrl+S',command=save_file)#creating the label for save file and shortcut key
filemenu.add_command(label='Save As',accelerator='Ctrl+Alt+S',command=saveas_file)#creating the label for save as file and shortcut key
filemenu.add_command(label='Print',accelerator='Ctrl+P',command=printout)#creating the label for print file and shortcut key

#toolbar section
tool_bar=Label(root)
tool_bar.pack(side=TOP,fill=X)
font_families=font.families()
font_family_variable=StringVar()
fontfamily_Combobox=Combobox(tool_bar,width=30,values=font_families,state='readonly',textvariable=font_family_variable)
fontfamily_Combobox.current(font_families.index('Arial'))
fontfamily_Combobox.grid(row=0,column=0,padx=5)
size_variable=IntVar()
font_size_Combobox=Combobox(tool_bar,width=14,textvariable=size_variable,state='readonly',values=tuple(range(8,81)))
font_size_Combobox.current(4)
font_size_Combobox.grid(row=0,column=1,padx=5)
fontfamily_Combobox.bind('<<ComboboxSelected>>',font_style)
font_size_Combobox.bind('<<ComboboxSelected>>',font_size)

#buttons section
print("Current Working Directory:", os.getcwd())
print("File Exists:", os.path.exists("bold.png"))

boldImage=PhotoImage(file='bold.png')#adding the image for the bold font 
boldButton=Button(tool_bar,image=boldImage,command=bold_text)
boldButton.grid(row=0,column=2,padx=5)#creating the grid for the button in the tab

italicImage=PhotoImage(file='italic.png')#adding the image for the italic font 
italicButton=Button(tool_bar,image=italicImage,command=italic_text)
italicButton.grid(row=0,column=3,padx=5)#creating the grid for the button in the tab

underlineImage=PhotoImage(file='underline.png')#adding the image for the underline font 
underlineButton=Button(tool_bar,image=underlineImage,command=underline_text)
underlineButton.grid(row=0,column=4,padx=5)#creating the grid for the button in the tab

fontColorImage=PhotoImage(file='font_color.png')#adding the image for the coloring of the text
fontColorButton=Button(tool_bar,image=fontColorImage,command=color_select)
fontColorButton.grid(row=0,column=5,padx=5)#creating the grid for the button in the tab

leftAlignImage=PhotoImage(file='left.png')#adding the image for the left alignment 
leftAlignButton=Button(tool_bar,image=leftAlignImage,command=align_left)
leftAlignButton.grid(row=0,column=6,padx=5)#creating the grid for the button in the tab

rightAlignImage=PhotoImage(file='right.png')#adding the image for the right alignment
rightAlignButton=Button(tool_bar,image=rightAlignImage,command=align_right)
rightAlignButton.grid(row=0,column=7,padx=5)#creating the grid for the button in the tab

centerAlignImage=PhotoImage(file='center.png')#adding the image for the center alignment
centerAlignButton=Button(tool_bar,image=centerAlignImage,command=align_center)
centerAlignButton.grid(row=0,column=8,padx=5)#creating the grid for the button in the tab

scrollbar=Scrollbar(root)
scrollbar.pack(side=RIGHT,fill=Y)
textarea=Text(root,yscrollcommand=scrollbar.set,font=('arial',12),undo=True)
textarea.pack(fill=BOTH,expand=True)
scrollbar.config(command=textarea.yview)

status_bar=Label(root,text='Status Bar')#creates the label for the status bar   
status_bar.pack(side=BOTTOM)# MAKES THE POSITION FIXED TO THE BUTTON OF THE SCREEN AND PACKS IT 


textarea.bind('<<Modified>>',statusBarFunction)# to update the status bar at the button everytime text is being edited which includes word count and other

editmenu=Menu(menubar,tearoff=False)
editmenu.add_command(label='Undo',accelerator='Ctrl+Z')#creating the command of UNDO and adding the shortcut key
editmenu.add_command(label='Cut',accelerator='Ctrl+X',command=lambda :textarea.event_generate('<Control x>'))#creating the command of CUT and adding the shortcut key
editmenu.add_command(label='Copy',accelerator='Ctrl+C',command=lambda :textarea.event_generate('<Control c>'))#creating the command of COPY AND Adding the shortcut key
editmenu.add_command(label='Paste',accelerator='Ctrl+V',command=lambda :textarea.event_generate('<Control v>'))#creating the command of paste and adding shorcut key for it
editmenu.add_command(label='Select All',accelerator='Ctrl+A')#creating the command of SELECT ALL and adding the shortcut key
editmenu.add_command(label='Clear',accelerator='Ctrl+Alt+X',command=lambda :textarea.delete(0.0,END))#CLEARING THE TEXT

menubar.add_cascade(label='Edit',menu=editmenu)#ADDS EDIT TO THE MENU


root.bind("<Control-o>",open_file)#binds the open file to the "control" and "o"
root.bind("<Control-n>",new_file)#binds the NEW file to the "control" and "N"
root.bind("<Control-s>",save_file)#binds the SAVE file to the "control" and "S"
root.bind("<Control-Alt-s>",saveas_file)#binds the save as file to the "control", "ALT"and "S"
root.bind("<Control-p>",printout)#binds the PRINT file to the "control" and "P"

root.mainloop()#CREATES THE CONTINUOS LOOP IN THE PROGRAM



