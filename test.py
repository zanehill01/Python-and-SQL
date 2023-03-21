import tkinter
import tkinter.messagebox
import pyodbc

class SQLGUI:
    def __init__(self):

        self.main_window = tkinter.Tk()

        # create window

        self.main_window.geometry('275x75')
        self.main_window.title('SQL Server Login')

        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
        self.last_frame = tkinter.Frame(self.main_window)

        self.label1 = tkinter.Label(self.top_frame, text='Login:')
        self.entry1 = tkinter.Entry(self.top_frame, width=30)

        self.label2 = tkinter.Label(self.bottom_frame, text='Password:')
        self.entry2 = tkinter.Entry(self.bottom_frame, width=30, show='*')
        
        self.loginbutton = tkinter.Button(self.last_frame, text='Login', command=self.do_something)

        #

        self.top_frame.pack()
        self.bottom_frame.pack()
        self.last_frame.pack()

        self.label1.pack(side='left')
        self.entry1.pack(side='left')

        self.label2.pack(side='left')
        self.entry2.pack(side='left')

        self.loginbutton.pack()

        #

        tkinter.mainloop()

    def do_something(self):

        tkinter.messagebox.showinfo('Response', 'Logged In!')

        login = self.entry1.get()
        pw = self.entry2.get()

        self.main_window.destroy()

        preList = {}
        courseList = []
        cn_str = (

        'Driver={SQL Server Native Client 11.0};'
        'Server=MIS-SQLJB'
        'Database=School;' 
        'UID='+login+';'
        'PWD='+pw+';'   

        )

        # connect to server

        cn = pyodbc.connect(cn_str)

        cursor = cn.cursor()
        cursor.execute('Select * From School.dbo.Course')

myinstance = SQLGUI()

print('Done!')