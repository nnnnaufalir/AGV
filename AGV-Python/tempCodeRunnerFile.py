import tkinter as tk
from tkinter import ttk


Large_Font=("Verdana",16)

class First(tk.Tk):#inherited tk.Tk
    def __init__(self, *args,**kwargs):
        tk.Tk.__init__(self,*args,**kwargs)

       # self.iconbitmap(default='favicon.ico')
        tk.Tk.wm_title(self,"First one!")

        container = tk.Frame(self)#always have this, frame is predef frame is edge of window
        container.pack(side="top",fill="both",expand=True)# fill is for limits you set and expand is to go beyond if needed
        container.grid_rowconfigure(0,weight=1)#0 is min value, weight specs priority
        container.grid_columnconfigure(0,weight=1)

        self.frames={}
        for F in (StartPage, PageOne, PageTwo, PageThree):

            frame = F(container,self)
            self.frames[F]=frame
            frame.grid(row=0,column=0,sticky="ew")

        self.show_frame(StartPage)

    def show_frame(self,cont):
        frame=self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)

        label=ttk.Label(self,text="Hello World",font=Large_Font)
        label.pack(pady=10,padx=10)

        button = ttk.Button(self,text="PageOne", command=lambda: controller.show_frame(PageOne))
        button.pack()

        button1=ttk.Button(self,text="PageTwo",command=lambda: controller.show_frame(PageTwo))
        button1.pack()

        button2=ttk.Button(self,text="Page Three",command= lambda: controller.show_frame(PageThree))
        button2.pack()

class PageOne(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label=tk.Label(self,text="Welcome to Page 1",font=Large_Font)
        label.pack(pady=10,padx=10)

        button = ttk.Button(self,text="To Home", command=lambda: controller.show_frame(StartPage))
        button.pack()

        button1 = ttk.Button(self,text="To PageTwo", command=lambda: controller.show_frame(PageTwo))
        button1.pack()

class PageTwo(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label=tk.Label(self,text="Welcome to Page 2",font=Large_Font)
        label.pack(pady=10,padx=10)

        button = ttk.Button(self,text="To Home", command=lambda: controller.show_frame(StartPage))
        button.pack()

        button1 = ttk.Button(self,text="To PageOne", command=lambda: controller.show_frame(PageOne))
        button1.pack()


class PageThree(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)

        label=ttk.Label(self,text="Graph page",font=Large_Font)
        label.pack(pady=10,padx=10)

        button = ttk.Button(self,text="To Home", command=lambda: controller.show_frame(StartPage))
        button.pack()

        button1 = ttk.Button(self,text="To PageOne", command=lambda: controller.show_frame(PageOne))
        button1.pack()




app=First()
app.mainloop()