



from tkinter import *
from tkinter.ttk import Notebook,Progressbar,Combobox
import threading
import time
from tkinter import filedialog
from PIL import Image
import tkinter.messagebox





class ConvertingImage:
    def __init__(self,root):
        self.root=root
        self.root.title("Image Converter")
        self.root.geometry("500x300")
        self.root.iconbitmap("logo328.ico")
        self.root.resizable(0,0)


        save=StringVar()
        size=StringVar()


        def on_enter1(e):
            but_browse['background']="black"
            but_browse['foreground']="cyan"  
        def on_leave1(e):
            but_browse['background']="SystemButtonFace"
            but_browse['foreground']="SystemButtonText"

            

        def on_enter2(e):
            but_convert_png['background']="black"
            but_convert_png['foreground']="cyan"  
        def on_leave2(e):
            but_convert_png['background']="SystemButtonFace"
            but_convert_png['foreground']="SystemButtonText"

        def on_enter3(e):
            but_convert_jpg['background']="black"
            but_convert_jpg['foreground']="cyan"  
        def on_leave3(e):
            but_convert_jpg['background']="SystemButtonFace"
            but_convert_jpg['foreground']="SystemButtonText"

        def on_enter4(e):
            but_clear['background']="black"
            but_clear['foreground']="cyan"  
        def on_leave4(e):
            but_clear['background']="SystemButtonFace"
            but_clear['foreground']="SystemButtonText"

        
        def clear():
            save.set("")
            size.set("Select Size")
            lab.config(text="")



    #==============================command=======================================#

        def browse():
           global filename
           file_path = filedialog.askopenfilename(title = "Select file",filetypes = (("png","*.png"),("jpg","*.jpg"),("all files","*.*")))
           if len(file_path)!=0:
               lab.config(text="file is selected")
           filename=file_path


        def convert_jpg():
            try:

                if save.get()!="":
                    if size.get()!="Select Size":
                        im = Image.open(filename)
                        s=size.get()
                        d=s.split(",")                       
                        img = im.resize((int(d[0]),int(d[1])),Image.ANTIALIAS)
                        img = img.convert('RGB')
                        img.save('{}.jpg'.format(save.get()),format='JPEG')
                    else:
                        tkinter.messagebox.showerror("Error","Please Select the size")
                    
                else:
                    tkinter.messagebox.showerror("Error","please enter Image name to save")
            except Exception as e:
                print(e)

        def jpg_thread():
            t1=threading.Thread(target=convert_jpg)
            t1.start()


        def convert_png():
            if save.get()!="":
                if size.get()!="Select Size":
                    im = Image.open(filename)
                    s=size.get()
                    d=s.split(",")
                    img = im.resize((int(d[0]),int(d[1])),Image.ANTIALIAS)
                    img = img.convert('RGB')
                    img.save('{}.png'.format(save.get()),format='PNG')
                else:
                    tkinter.messagebox.showerror("Error","Please Select the size")
            else:
                tkinter.messagebox.showerror("Error","please enter Image name to save")
                

        def png_thread():
            t1=threading.Thread(target=convert_png)
            t1.start()



    #========================frame========================================#
        mainframe=Frame(self.root,width=500,height=300,relief="ridge",bd=3)
        mainframe.place(x=0,y=0)

        top_frame=Frame(mainframe,width=495,height=265,relief="ridge",bd=3)
        top_frame.place(x=0,y=0)

        task_bar_frame=Frame(mainframe,width=495,height=30,relief="ridge",bd=3)
        task_bar_frame.place(x=0,y=265)

    #=====================================================================#

        lab_frame=LabelFrame(top_frame,text="Image resize",width=490,height=258,font=('times new roman',12,'bold'),bg="#1c45ea",fg="white")
        lab_frame.place(x=0,y=0)

    #========================lab_frame=============================================#

        but_browse=Button(lab_frame,text="Browse",width=15,font=('times new roman',12,'bold'),cursor="hand2",command=browse)
        but_browse.place(x=20,y=10)
        but_browse.bind("<Enter>",on_enter1)
        but_browse.bind("<Leave>",on_leave1)

        lab=Label(lab_frame,text="",font=('times new roman',12),bg="#1c45ea",fg="white")
        lab.place(x=190,y=14)

        

        but_clear=Button(lab_frame,text="Clear",width=15,font=('times new roman',12,'bold'),cursor="hand2",command=clear)
        but_clear.place(x=330,y=10)
        but_clear.bind("<Enter>",on_enter4)
        but_clear.bind("<Leave>",on_leave4)
    

        size_list=['728,90','468,60','320,50','300,100','300,50','234,60','300,600'\
            ,'160,600','120,600','240,400','120,240','336,280','300,250','250,250',\
            '200,200','180,150','125,125','120,90','120,60','88,31','160,160','176,208',\
            '240,320','320,240','320,320','352,416','416,352','320,480','480,320','320,416',\
            '480,268','320,480','960,640','1136,640','1024,600','1024,768','2048,1536','320,200',\
            '640,200','640,350','640,480','720,348','1024,768','1280,1024','1366,768','1600,1200',\
            '1680,1050','1920,1200','576,486','720,486','143,59','150,112','100,75','75,100','180,240',\
            '375,500','768,1024']
        En_len=Combobox(lab_frame,values=size_list,font=('arial',10),width=14,state="readonly",textvariable=size)
        En_len.set("Select Size")
        En_len.place(x=180,y=60)


        lab_enter_name=Label(lab_frame,text="Enter Name to save",font=('times new roman',11,'bold'),bg="#1c45ea",fg="white")
        lab_enter_name.place(x=180,y=120)

        ent_name=Entry(lab_frame,width=18,font=('times new roman',14,'bold'),relief="ridge",bd=3,textvariable=save)
        ent_name.place(x=150,y=150)

        but_convert_jpg=Button(lab_frame,text="Convert-JPG",width=15,font=('times new roman',12,'bold'),cursor="hand2",command=jpg_thread)
        but_convert_jpg.place(x=20,y=190)
        but_convert_jpg.bind("<Enter>",on_enter3)
        but_convert_jpg.bind("<Leave>",on_leave3)


        but_convert_png=Button(lab_frame,text="Convert-PNG",width=15,font=('times new roman',12,'bold'),cursor="hand2",command=png_thread)
        but_convert_png.place(x=330,y=190)
        but_convert_png.bind("<Enter>",on_enter2)
        but_convert_png.bind("<Leave>",on_leave2)

    #=============================task_bar=========================================================#

        prg=Progressbar(task_bar_frame,length=489,orient=HORIZONTAL,mode='indeterminate')
        prg.place(x=0,y=0)


if __name__ == "__main__":
    root=Tk()
    app=ConvertingImage(root)
    root.mainloop()
