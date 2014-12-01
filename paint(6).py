from Tkinter import *
import tkFileDialog
import Image,ImageDraw, ImageTk
from tkColorChooser import askcolor

class MyDialog:

    tex=""

    def __init__(self, parent):

        top = self.top = Toplevel(parent,bg="white",bd=0)
        Label(top).pack()

        self.e = Entry(top)
        self.e.pack(padx=5)

        b = Button(top, text="Create", command=self.ok)
        b.pack(pady=5)

    def ok(self):

        self.tex=self.e.get()
        self.top.destroy()


def onObjectClick(event):
    global curr_object
    if curr_object is not None:
        for i in curr_object:        
            drawing_area.itemconfig(i,dash=(),width=1)
    curr_object=event.widget.find_overlapping(event.x-5, event.y-5,event.x+5,event.y+5)
    drawing_area.itemconfig(curr_object,dash=(5,3),width=3)



def restore():
    drawing_area.delete(select_object)
    if (curr_object is not None and type(curr_object)==int):
        drawing_area.itemconfig(curr_object,dash=(),width=1)
    
    elif curr_object is not None:
            for i in curr_object:
                drawing_area.itemconfig(i,dash=(),width=1)
                select_value=0

class Example(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent)   
         
        self.parent = parent        
        self.initUI()
        
    def initUI(self):
      
        self.parent.title("Paint Software")
        
        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)

        status = Label(self.parent, text="", bd=1, relief=SUNKEN, anchor=W)
        status.pack(side=BOTTOM, fill=X)
        fileMenu = Menu(menubar)
        fileMenu.add_command(label="New", command=self.onNew)
        fileMenu.add_command(label="Open", command=self.onOpen)
        fileMenu.add_command(label="Save", command=self.onSave)
        fileMenu.add_command(label="SaveAs", command=self.onSaveAs)
        fileMenu.add_separator()
        fileMenu.add_command(label="Exit", command=self.onExit)
        menubar.add_cascade(label="File", menu=fileMenu)
        editmenu = Menu(menubar)
        #editmenu.add_command(label="Undo", command=donothing)
        editmenu.add_separator()
        editmenu.add_command(label="Cut", command=self.cut)
        editmenu.add_command(label="Copy", command=self.copy)
        editmenu.add_command(label="Paste", command=self.paste)
        editmenu.add_command(label="Clear", command=self.onclear)
        menubar.add_cascade(label="Edit", menu=editmenu)
        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Help Index", command=self.donothing)
        helpmenu.add_command(label="About...", command=self.donothing)
        menubar.add_cascade(label="Help", menu=helpmenu)
        self.parent.config(menu=menubar)
        toolbar = Frame(self.parent, bd=1, relief=RAISED)
        toolbar.pack(side=TOP, fill=X)
        self.parent.config(menu=menubar)
        toolbar = Frame(self.parent, bd=1, relief=RAISED,bg="white")

        b2=Button(toolbar,image=oval1,relief=FLAT,command=self.oval)
        b2.image=oval1
        b2.pack(side=LEFT, padx=1, pady=1)
        b3=Button(toolbar, image=rectangle1,relief=FLAT,command=self.rectangle)
        b3.image=rectangle1
        b3.pack(side=LEFT, padx=1, pady=1)
        b4=Button(toolbar, text="LINE",relief=FLAT,command=self.createline)
        b4.pack(side=LEFT, padx=1, pady=1)
        b4=Button(toolbar, image=line1,relief=FLAT,command=self.Line)
        b4.image=line1
        b4.pack(side=LEFT, padx=1, pady=1)
        b7=Button(toolbar, image=triangle1,relief=FLAT,command=self.triangle)
        b7.image=triangle1
        b7.pack(side=LEFT, padx=1, pady=1)
        b8=Button(toolbar, image=eraser,command=self.eraser,bg="white", bd=1)
        b8.image=eraser
        b8.pack(side=LEFT, padx=1, pady=1)
        b5=Button(toolbar,text="thicker ", command=self.incr_width, bd=0,bg="white")
        b5.pack(side=LEFT, padx=1, pady=1)
        b6=Button(toolbar,text="thinner" , command=self.decr_width, bd=0,bg="white")
        b6.pack(side=LEFT, padx=1, pady=1)
        b10=Button(toolbar,text="SELECT" , command=self.select, bd=0,bg="white")
        b10.pack(side=LEFT, padx=1, pady=1)
        b11=Button(toolbar,text="TEXT" , command=self.textbox, bd=0,bg="white")
        b11.pack(side=LEFT, padx=1, pady=1)
        b16=Button(toolbar,text="FILL", command=self.fill,bg="white", bd=1)
        b16.pack(side=LEFT, padx=1, pady=1)
        b16=Button(toolbar, command=self.outline, bd=0,text="OUTLINE", bg="white")
        b16.pack(side=LEFT, padx=1, pady=1)
        b15=Button(toolbar, command=self.callback_red, bd=0,bg="red")
        b15.pack(side=LEFT, padx=1, pady=1)
        b14=Button(toolbar,command=self.callback_blue, bd=0,bg="blue")
        b14.pack(side=LEFT, padx=1, pady=1)
        b13=Button(toolbar, command=self.callback_green, bd=0,bg="green")
        b13.pack(side=LEFT, padx=1, pady=1)
        
        b12=Button(toolbar,text="Choose Color",fg="darkgreen", command=self.callback)
        b12.pack(side=LEFT, padx=1, pady=1)
        toolbar.pack(side=TOP, fill=X) 
        self.pack()

    def fill(self):
        global color_val
        color_val="fill"

    def outline(self):
        global color_val
        color_val="outline"

    def cut(self):
        self.copy=0
        self.cut=1
        global pastex,pastey
        pastex=(selectx0+selectx1)/2
        pastey=(selecty0+selecty1)/2

    def copy(self):
        self.cut=0
        self.copy=1
        global pastex,pastey
        pastex=(selectx0+selectx1)/2
        pastey=(selecty0+selecty1)/2

    def paste(self):
        if (self.cut==1 and curr_object is not None and type(curr_object) is not int):
            for i in curr_object:
                drawing_area.move(i,pastex,pastey)
            drawing_area.move(select_object,pastex,pastey)

        if (self.copy==1 and curr_object is not None and type(curr_object) is not int):        
            for i in curr_object:
                cordinates=drawing_area.coords(i)
                if len(cordinates)==2:
                    temp_text=drawing_area.itemcget(i,"text")
                    drawing_area.create_text(cordinates[0]+pastex,cordinates[1]+pastey,text=temp_text)

                if len(cordinates)==4 :
                    print cordinates,'b'
                    cordinates[0]=cordinates[0]+pastex
                    cordinates[1]=cordinates[1]+pastey
                    cordinates[2]=cordinates[2]+pastex
                    cordinates[3]=cordinates[3]+pastey
                    tag_list=drawing_area.gettags(i)
                    fill_color=drawing_area.itemcget(i,"fill")
                    if "crline" in tag_list:
                        drawing_area.create_line(cordinates[0],cordinates[1],cordinates[2],cordinates[3],fill=fill_color)
                    if "rectangle" in tag_list:
                        loc_color=drawing_area.itemcget(i,"outline")
                        drawing_area.create_rectangle(cordinates[0],cordinates[1],cordinates[2],cordinates[3],outline=loc_color,fill=fill_color)
                    if "oval" in tag_list:
                        loc_color=drawing_area.itemcget(i,"outline")
                        drawing_area.create_oval(cordinates[0],cordinates[1],cordinates[2],cordinates[3],outline=loc_color,fill=fill_color)
              
            ##if select_object is not None:
            


    def createline(self):
        global parameter
        parameter="crline"
     
    def callback_red(self):
        verify=0
        global color
        color="red"
        if (type(curr_object)==int):
            if(color_val=="outline"):
                drawing_area.itemconfig(curr_object,outline="red")
            elif(color_val=="fill"):
                drawing_area.itemconfig(curr_object,fill="red")
            return
        
        if curr_object is not None:
            for i in curr_object:
                for j in drawing_area.gettags(i):
                    if ("eraser"==str(j) or j=="line"):
                        verify=1
                if verify is not 1:
                    if(color_val=="outline"):
                        drawing_area.itemconfig(i,outline="red")
                    elif(color_val=="fill"):
                        drawing_area.itemconfig(i,fill="red")
                verify=0
                
    def callback_green(self):

        global color
        verify=0
        color="green"
        if (type(curr_object)==int):
            if(color_val=="outline"):
                drawing_area.itemconfig(curr_object,outline="green")
            elif(color_val=="fill"):
                drawing_area.itemconfig(curr_object,fill="green")
            return

        if curr_object is not None:
            for i in curr_object:
                for j in drawing_area.gettags(i):
                    if ("eraser"==str(j) or j=="line"):
                        verify=1
                if verify is not 1:
                    if(color_val=="outline"):
                        drawing_area.itemconfig(i,outline="green")
                    elif(color_val=="fill"):
                        drawing_area.itemconfig(i,fill="green")
                verify=0
    def callback_blue(self):
        global color
        verify=0
        color="blue"
        if (type(curr_object)==int):
            if(color_val=="outline"):
                drawing_area.itemconfig(curr_object,outline="blue")
            elif(color_val=="fill"):
                drawing_area.itemconfig(curr_object,fill="blue")
            return

        if curr_object is not None:
            for i in curr_object:
                for j in drawing_area.gettags(i):
                    if ("eraser"==str(j) or j=="line"):
                        verify=1
                if verify is not 1:
                    if(color_val=="outline"):
                        drawing_area.itemconfig(i,outline="blue")
                    elif(color_val=="fill"):
                        drawing_area.itemconfig(i,fill="blue")
                verify=0
    def incr_width(self):
        global br_size,er_size
        if(parameter=="eraser"):
            er_size=er_size+5
        else:
            br_size=br_size+0.5

    def decr_width(self):
        global br_size,er_size
        if(parameter=="eraser" and er_size>5):
            er_size=er_size-5
        elif (parameter=="Line" and br_size>1):
            br_size=br_size-0.5
        
    def oval(self):
        global parameter,curr_object, xnew,ynew, resize
        
        resize=0
        parameter="oval"
        curr_object=None
        xnew=None
        ynew=None
        restore()

    def rectangle(self):
        
        global parameter, curr_object, xnew,ynew,resize
        resize=0
        parameter="rectangle"
        curr_object=None
        xnew=None
        ynew=None
        restore()

    def triangle(self):
        
        global parameter, curr_object, xnew,ynew, resize
        resize=0
        parameter="triangle"
        curr_object=None
        xnew=None
        ynew=None
        restore()

    def Line(self):
        restore()
        global parameter, xnew,ynew,resize
        resize=0
        parameter="Line"
        xnew=None
        ynew=None

    
    def eraser(self):
        global parameter, xnew,ynew,resize
        resize=0
        parameter="eraser"
        xnew=None
        ynew=None

    def textbox(self):
        global parameter,xnew,ynew
        parameter="textbox"
        xnew=None
        ynew=None
        
    def select(self):
        global parameter, curr_object, xnew,ynew
        parameter="select"
        deselect()
        curr_object=None
        xnew=None
        ynew=None

    def onclear(self):
        clear()
    def onNew(self):
        clear() 
    def callback(self):
        global color
        verify=0
        result = askcolor(color="#6A9662", 
                          title = "Bernd's Colour Chooser")
        print result
        color=result[1]
        #drawing_area.create_rectangle(100,100,100,100,outline=result[1])
        if (type(curr_object)==int):
            if(color_val=="outline"):
                drawing_area.itemconfig(curr_object,outline=color)
            elif(color_val=="fill"):
                drawing_area.itemconfig(curr_object,fill=color)
            return

        if curr_object is not None:
            for i in curr_object:
                for j in drawing_area.gettags(i):
                    if ("eraser"==str(j) or j=="line"):
                        verify=1
                if verify is not 1:
                    if(color_val=="outline"):
                        drawing_area.itemconfig(i,outline=color)
                    elif(color_val=="fill"):
                        drawing_area.itemconfig(i,fill=color)
                verify=0

        
        
        #root.configure(background=result[1])
   
    def donothing(self):        
        sys.exit()
        
    def onExit(self):
        sys.exit() 

    

    def onSave(self):
        save1()
    def onSaveAs(self):
        save()

    def onOpen(self):
        Open() 


    
    
def main():
    global draw
    global image
    #add_colour(root)
    image=Image.new("RGB",(1200,1200),(255,255,255))
    draw=ImageDraw.Draw(image)
    #add_colour(root)
    drawing_area.bind("<Motion>", motion)
    drawing_area.bind("<ButtonPress-1>", b1down)
    drawing_area.bind("<ButtonRelease-1>", b1up)
    drawing_area.bind("<Button-3>",rightclick)
    drawing_area.pack()
    root.mainloop()


def rightclick(event):
    print "copying"
    global pastex,pastey
    pastex=event.x-pastex
    pastey=event.y-pastey

def b1down(event):
    global b1, select_value,resize,xnew,ynew,xold1,yold1, check,curr_object

    if(type(curr_object)==int):
        cordinates=drawing_area.coords(curr_object)
        xold1=cordinates[0]
        yold1=cordinates[1]
        xnew=cordinates[2]
        ynew=cordinates[3]

 
    elif(curr_object is not None):
        xold1=selectx0
        yold1=selecty0
        xnew=selectx1
        ynew=selecty1    
        
    if (xnew is not None and ynew is not None and curr_object is not None and event.x>=xnew-50 and event.x<=xnew+50 and event.y<ynew and event.y>yold1):
        resize=1
    elif (xnew is not None and ynew is not None and curr_object is not None and event.x>=xold1-50 and event.x<=xold1+50 and event.y<ynew and event.y>yold1):
        resize=2
    elif (xnew is not None and ynew is not None and curr_object is not None and event.y>=ynew-50 and event.y<=ynew+50 and event.x<xnew and event.x>xold1):
        resize=3
    elif (xnew is not None and ynew is not None and curr_object is not None and event.y>=yold1-50 and event.y<=yold1+50 and event.x<xnew and event.x>xold1):
        resize=4
    else:
        resize=0

    if (parameter=="select" and check==0 and event.x>=min(selectx0,selectx1) and event.x<=max(selectx0,selectx1) and event.y>=min(selecty0,selecty1) and event.y<=max(selecty0,selecty1)):
        check=3


    if resize==0 and check is not 3:
        drawing_area.delete(select_object)

    if curr_object is not None and check is not 3:
        if (type(curr_object)==int):
            drawing_area.itemconfig(curr_object,dash=(),width=1)
            curr_object=None
            select_value=0
        else:
            for i in curr_object:
                drawing_area.itemconfig(i,dash=(),width=1)
            curr_object=None
            select_value=0
            
        
        
##    global curr_object
##    if (parameter is not "select"):
##        if (curr_object is not None and select_value==1 and parameter is not "move"):
##            for i in curr_object:
##                for j in drawing_area.gettags(i):
##                    if ('eraser'==j):
##                        continue
##                drawing_area.itemconfig(i,dash=(),width=1)
##                select_value=0
##        if parameter is not "move":        
##            curr_object=None
##        if parameter is not "move":
##            curr_object=event.widget.find_overlapping(event.x-5, event.y-5,event.x+5,event.y+5)
##        if curr_object is not None and parameter is not "eraser" and parameter is not "move":
##            for i in curr_object:
##                drawing_area.itemconfig(i,dash=(50,5),width=3)
##                select_value=1
    b1 = "down"           # you only want to draw when the button is down
                          # because "Motion" events happen -all the time-

def b1up(event):
    global check,curr_object, select_value, parameter, var, selectx0,selectx1,selecty0,selecty1,select_object
    global xnew,ynew,b1, xold, yold, xold1, yold1    
    if (parameter=="oval" and check==1):
            check=0
            print xold,yold,event.x, event.y
            xnew=event.x
            ynew=event.y
            xold1=xold
            yold1=yold
            
            drawing_area.coords(curr_object,xold,yold,event.x,event.y)
            drawing_area.itemconfig(curr_object,outline=color,dash=(),tags=("oval"))
            draw.ellipse(((xold,yold),(event.x,event.y)),outline=color)
    if (parameter=="rectangle" and check==1):
            check=0
            print xold,yold,event.x, event.y
            xnew=event.x
            ynew=event.y
            xold1=xold
            yold1=yold
            drawing_area.coords(curr_object,xold,yold,event.x,event.y)
            drawing_area.itemconfig(curr_object,dash=(),outline=color, tags=("rectangle"))
            draw.rectangle([xold,yold,event.x,event.y],outline=color)

    if (parameter=="crline" and check==1):
            check=0
            print xold,yold,event.x, event.y
            xnew=event.x
            ynew=event.y
            xold1=xold
            yold1=yold
            drawing_area.coords(curr_object,xold,yold,event.x,event.y)
            drawing_area.itemconfig(curr_object,dash=(),fill=color, tags=("crline"))
            draw.rectangle([xold,yold,event.x,event.y],outline=color)

           
    if (parameter=="textbox" and check==1):
        
            
            check=0
            parameter="NONE"
            #Label(root).grid(row=0, sticky=W)
            #e1 = Entry(root)
            #e1.grid(row=0, column=1)
            # Get the content of the e1 entry
            #content = e1.get()
            #mainloop()
            d = MyDialog(root)
            root.wait_window(d.top)
            event.widget.create_text((event.x+xold)/2,(event.y+yold)/2,text=str(d.tex),tags=("textbox"))
            paremeter="textbox"
            drawing_area.delete(curr_object)

    if (parameter=="triangle" and check==1):
            check=0
            print xold,yold,event.x, event.y
            drawing_area.coords(curr_object,xold,event.y,(event.x+xold)/2,yold,event.x,event.y)
            drawing_area.itemconfig(curr_object,outline=color,dash=())
            draw.polygon([(xold,event.y),((event.x+xold)/2,yold),(event.x,event.y)],outline=color)

    if (parameter=="select" and check==3 and resize==0):
        check=0
    
        
    if (parameter=="select" and check==1 and resize==0):
            check=0
            print xold,yold,event.x, event.y
            selectx0=xold
            selectx1=event.x
            selecty0=yold
            selecty1=event.y
            verify=0
            deselect()
            if xold is not None and yold is not None:
                curr_object=event.widget.find_overlapping(xold, yold,event.x,event.y)
            else:
                curr_object=event.widget.find_overlapping(event.x-5,event.y-5,event.x+5,event.y+5)

            if curr_object is not None:
                for i in curr_object:
                    temp_list=drawing_area.gettags(i)
                    if ("eraser" in temp_list or "line" in temp_list):
                        continue
                    drawing_area.itemconfig(i,dash=(50,5),width=3)
                    select_value=1

            drawing_area.delete(select_object)
            select_object=drawing_area.create_rectangle(selectx0,selecty0,selectx1,selecty1,dash=(3,5))
                    

    if (parameter=="eraser" and check==1):
        check=0
        drawing_area.delete(eraser_object)

    b1 = "up"
    xold = None           # reset the line when you let go of the button
    yold = None

def deselect():
    global curr_object
    if curr_object is not None:
        if (type(curr_object)==int):
            drawing_area.itemconfig(curr_object,dash=(),width=1)
            curr_object=None
            select_value=0
        else:
            for i in curr_object:
                drawing_area.itemconfig(i,dash=(),width=1)
            curr_object=None
            select_value=0
    curr_object=None
    
def Open():
    global filename
    
    dirname = tkFileDialog.askdirectory(parent=root,initialdir="/",title='Please select a directory')
    if len(dirname ) > 0:
        print "You chose %s" % dirname
    file = tkFileDialog.askopenfile(parent=root,mode='rb',title='Choose a file')
    print "ll"
    print file
    
       
    pilImage = Image.open(file)
    photo = ImageTk.PhotoImage(pilImage)
    imagesprite = drawing_area.create_image(600,600,image=photo)
    #add_colour(root)
    print "dd"
    
    root.mainloop()
def save():
        master = Tk()
        

        e = Entry(master)
        e.pack()

        e.focus_set()

        def callback():
            global filename
            filename = e.get()
            image.save(filename)
            master.destroy()

        b = Button(master, text="Save", width=10, command=callback)
        b.pack()

        mainloop()
                
        

        print "rr"
def save1():
    print filename
    #filename = "temp.gif"
    image.save(filename)
    print "rr"
def clear():
        drawing_area.delete("all")
        image=Image.new("RGB",(1200,1200),(255,255,255))
        draw=ImageDraw.Draw(image)

def motion(event):
    global xnew, ynew, xold, yold, check, curr_object, eraser_object, select_value, selectx0, selectx1, selecty0, selecty1,xold1,yold1,select_object

    ##print xold,yold,xnew,ynew,event.x,event.y,xold1,yold1    


    if(curr_object is not None and resize==1 and b1=="down"):
        if (type(curr_object)==int):
            cordinates=drawing_area.coords(curr_object)
            print cordinates,'a'
            cordinates[2]=event.x
            drawing_area.coords(curr_object,cordinates[0],cordinates[1],cordinates[2],cordinates[3])
        else:
            delta=event.x-selectx1
            selectx1=event.x
            drawing_area.coords(select_object,selectx0,selecty0,event.x,selecty1)
            for i in curr_object:
                cordinates=drawing_area.coords(i)
                if len(cordinates)==2:
                    drawing_area.move(i,delta,0)

                elif len(cordinates)>0 :
                    print cordinates,'b'
                    cordinates[2]=cordinates[2]+delta
                    drawing_area.coords(i,cordinates[0],cordinates[1],cordinates[2],cordinates[3])
        return
    
    if(curr_object is not None and resize==2 and b1=="down"):
        if (type(curr_object)==int):
            cordinates=drawing_area.coords(curr_object)
            print cordinates
            cordinates[0]=event.x
            drawing_area.coords(curr_object,cordinates[0],cordinates[1],cordinates[2],cordinates[3])
        else:
            delta=event.x-selectx0
            selectx0=event.x
            drawing_area.coords(select_object,event.x,selecty0,selectx1,selecty1)
            for i in curr_object:
                cordinates=drawing_area.coords(i)
                if len(cordinates)==2:
                    drawing_area.move(i,delta,0)

                elif len(cordinates)>0 :
                    print cordinates
                    cordinates[0]=cordinates[0]+delta
                    drawing_area.coords(i,cordinates[0],cordinates[1],cordinates[2],cordinates[3])
                
        return

    if(curr_object is not None and resize==3 and b1=="down"):
        if (type(curr_object)==int):
            cordinates=drawing_area.coords(curr_object)
            print cordinates
            cordinates[3]=event.y
            drawing_area.coords(curr_object,cordinates[0],cordinates[1],cordinates[2],cordinates[3])
        else:
            delta=event.y-selecty1
            selecty1=event.y
            drawing_area.coords(select_object,selectx0,selecty0,selectx1,event.y)
            for i in curr_object:
                cordinates=drawing_area.coords(i)
                if len(cordinates)==2:
                    drawing_area.move(i,0,delta)
                elif len(cordinates)>0 :
                    print cordinates
                    cordinates[3]=cordinates[3]+delta
                    drawing_area.coords(i,cordinates[0],cordinates[1],cordinates[2],cordinates[3])
                    #drawing_area.coords(select_object,selectx0,selecty0,selectx1,event.y)
        return

    if(curr_object is not None and resize==4 and b1=="down"):
        if (type(curr_object)==int):
            cordinates=drawing_area.coords(curr_object)
            print cordinates
            cordinates[1]=event.y
            drawing_area.coords(curr_object,cordinates[0],cordinates[1],cordinates[2],cordinates[3])
        else:
            delta=event.y-selecty0
            selecty0=event.y
            drawing_area.coords(select_object,selectx0,event.y,selectx1,selecty1)
            for i in curr_object:
                cordinates=drawing_area.coords(i)
                if len(cordinates)==2:
                    drawing_area.move(i,0,delta)
                elif len(cordinates)>0 :
                    print cordinates
                    cordinates[1]=cordinates[1]+delta
                    drawing_area.coords(i,cordinates[0],cordinates[1],cordinates[2],cordinates[3])
        return
        

    if (eraser_object is not None and parameter is not "eraser"):
        drawing_area.delete(eraser_object)

    if (b1=="down" and parameter is not "select" and select_value==1 and parameter is not "move"):
        if curr_object is not None:
            drawing_area.itemconfig(curr_object,dash=(),width=1)
            curr_object=None
            select_value=0
            

            
    if b1 == "down" and parameter=="Line":
        deselect()
        if xold is not None and yold is not None:
            event.widget.create_line(xold,yold,event.x,event.y,activefill="",fill=color,smooth=FALSE, width=br_size,tags=("line"))
            draw.line(((xold,yold),(event.x,event.y)),(0,128,0),width=3)
        xold = event.x
        yold = event.y

    elif (parameter=="eraser" and check==0):
        deselect()
        eraser_object=event.widget.create_rectangle(event.x-er_size/2,event.y-er_size/2,event.x+er_size/2,event.y+er_size/2,fill="",outline="black")
        check=1

    elif (parameter=="eraser" and check==1 and eraser_object is not None):
        if(b1=="down"):
            event.widget.create_rectangle(event.x-er_size/2,event.y-er_size/2,event.x+er_size/2,event.y+er_size/2,fill="white",outline="white",tags=("eraser"))
            draw.rectangle([event.x-er_size/2,event.y-er_size/2,event.x+er_size/2,event.y+er_size/2],fill=(255,255,255))
            
        drawing_area.coords(eraser_object,event.x-er_size/2,event.y-er_size/2,event.x+er_size/2,event.y+er_size/2)
    
    elif (parameter=="oval" and check==0 and b1=="down"):
        print "assign"
        xold=event.x
        print xold
        yold=event.y
        print yold
        check=2
        deselect()
        
    elif (parameter=="oval" and check==2 and b1=="down"):
        if xold==None:
            xold=event.x
        if yold==None:
            yold=event.y
        deselect()
        curr_object=event.widget.create_oval(xold,yold,event.x,event.y,dash=(3,5))
        check=1

    elif (parameter=="oval" and check==1 and b1=="down"):
            drawing_area.coords(curr_object,xold,yold,event.x,event.y) 
    

    elif (parameter=="crline" and check==0 and b1=="down"):
        print "assign"
        xold=event.x
        print xold
        yold=event.y
        print yold
        check=2

    elif (parameter=="crline" and check==2 and b1=="down"):
        if xold==None:
            xold=event.x
        if yold==None:
            yold=event.y
        curr_object=event.widget.create_line(xold,yold,event.x,event.y,dash=(3,5))
        check=1

    elif (parameter=="crline" and check==1 and b1=="down"):
        drawing_area.coords(curr_object,xold,yold,event.x,event.y) 



    elif (parameter=="rectangle" and check==0 and b1=="down"):
        print "assign"
        xold=event.x
        print xold
        yold=event.y
        print yold
        check=2

    elif (parameter=="rectangle" and check==2 and b1=="down"):
        if xold==None:
            xold=event.x
        if yold==None:
            yold=event.y
        curr_object=event.widget.create_rectangle(xold,yold,event.x,event.y,dash=(3,5))
        check=1

    elif (parameter=="rectangle" and check==1 and b1=="down"):
        drawing_area.coords(curr_object,xold,yold,event.x,event.y) 

        
    elif (parameter=="select" and check==3 and curr_object is not None and b1=="down"):
        deselect()
        print "moving"
        if xold is None:
            xold=event.x
        if yold is None:
            yold=event.y
        drawing_area.move(select_object,event.x-xold,event.y-yold)
        
        for i in curr_object:
            drawing_area.move(i,event.x-xold,event.y-yold)
            
        selectx0=selectx0+event.x-xold
        selectx1=selectx1+event.x-xold
        selecty0=selecty0+event.y-yold
        selecty1=selecty1+event.y-yold

        xold=event.x
        yold=event.y


    elif (parameter=="textbox" and check==0 and b1=="down"):
        print "assign"
        xold=event.x
        print xold
        yold=event.y
        print yold
        check=2

    elif (parameter=="textbox" and check==2 and b1=="down"):
        if xold==None:
            xold=event.x
        if yold==None:
            yold=event.y
        curr_object=event.widget.create_rectangle(xold,yold,event.x,event.y,dash=(3,5))
        check=1

    elif (parameter=="textbox" and check==1 and b1=="down"):
        drawing_area.coords(curr_object,xold,yold,event.x,event.y) 

    elif (parameter=="move" and check==0 and b1=="down"):
        print "assign"
        xold=event.x
        print xold
        yold=event.y
        print yold
        check=2

    elif (parameter=="move" and check==2 and b1=="down"):
        if xold==None:
            xold=event.x
        if yold==None:
            yold=event.y
        check=1



    elif (parameter=="select" and check==0 and b1=="down"):
        print "assign"
        xold=event.x
        print xold
        yold=event.y
        print yold
        check=2

    elif (parameter=="select" and check==2 and b1=="down"):
        if xold==None:
            xold=event.x
        if yold==None:
            yold=event.y
        deselect()            
        select_object=event.widget.create_rectangle(xold,yold,event.x,event.y,dash=(3,5))
        check=1

    elif (parameter=="select" and check==1 and b1=="down"):
        drawing_area.coords(select_object,xold,yold,event.x,event.y) 

    
    elif (parameter=="triangle" and check==0 and b1=="down"):
        print "assign"
        xold=event.x
        print xold
        yold=event.y
        print yold
        check=2

    elif (parameter=="triangle" and check==2 and b1=="down"):
        if xold==None:
            xold=event.x
        if yold==None:
            yold=event.y
        curr_object=event.widget.create_polygon(xold,event.y,(event.x+xold)/2,yold,event.x,event.y,dash=(3,5),fill="",outline="black")
        check=1

    elif (parameter=="triangle" and check==1 and b1=="down"):
        drawing_area.coords(curr_object,xold,event.y,(event.x+xold)/2,yold,event.x,event.y,) 

val=0
root = Tk()
drawing_area = Canvas(root,bg="white",selectbackground="blue",width=1200,height=600)
global draw
global image
oval1 = PhotoImage(file = "oval.gif")
print "smriti"
rectangle1 = PhotoImage(file = "rectangle.gif")
print "smriti"
line1 = PhotoImage(file = "line.gif")
print "smriti"
triangle1 = PhotoImage(file = "triangle.gif")
eraser = PhotoImage(file = "eraser.gif")
curr_object=None
check=0
select_value=0
color="black"
b1 = "up"
xold, yold = None, None
xold1, yold1=None, None
parameter="Line"
selectx0=0
selecty0=0
selectx1=0
selecty1=0
br_size=1
er_size=10
app=Example(root)
eraser_object=None
select_object=None
xnew=None
ynew=None
var=''
resize=0
pastex=None
pastey=None
color_val=None


if __name__ == "__main__":
    main()

