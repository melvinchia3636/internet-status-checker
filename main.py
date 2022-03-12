from tkinter import *
import tkinter.ttk as ttk
from ttkthemes import ThemedTk
import requests, socket

class Window(ThemedTk):
    def __init__(self, title):
        super().__init__(theme='clearlooks')
        self.geometry('300x170')
        self.title(title)
        self.config(bg='#efebe7')
        self.resizable(0, 0)

class TitleWindow(Window):
    def __init__(self):
        super().__init__('Internet Status')
        
        self.widgetSetup()
        self.gridSetup()
        
    def widgetSetup(self):
        self.widgetContainer = ttk.Frame(self)
        self.titleLabel = ttk.Label(self.widgetContainer, text='Internet Status Checker')
        self.requestBtn = ttk.Button(self.widgetContainer, text='Requests', width=10, command=Requests)
        self.socketBtn = ttk.Button(self.widgetContainer, text='Socket', width=10, command=Socket)
        
    def gridSetup(self):
        Grid.rowconfigure(self, 0, weight=1)
        Grid.columnconfigure(self, 0, weight=1)
        
        self.widgetContainer.grid()
        self.titleLabel.grid(row=0, column=0, pady=(0, 10))
        self.requestBtn.grid(row=1, column=0, pady=(10, 5))
        self.socketBtn.grid(row=2, column=0)
        
    def run(self):
        self.mainloop()

class WorkWindow(Window):
    def __init__(self, title):
        super().__init__(title)
        self.protocol("WM_DELETE_WINDOW", self.quitWin)

        self.widgetSetup()
        self.gridSetup()     
        
    def widgetSetup(self):
        self.statusContainer = ttk.Frame(self)
        self.statusDescLabel = ttk.Label(self.statusContainer, text="You're currently ")
        self.statusLabel = ttk.Label(self.statusContainer)
        
    def gridSetup(self):
        Grid.rowconfigure(self, 0, weight=1)
        Grid.columnconfigure(self, 0, weight=1)

        self.statusContainer.grid()
        self.statusDescLabel.grid(row=0, column=0)
        self.statusLabel.grid(row=0, column=1)
        
    def quitWin(self):
        self.after_cancel(self.after_ID) 
        self.destroy()
        
class Requests(WorkWindow):
    def __init__(self):
        super().__init__('Requests Method')
        self.getRequest()
        
    def getRequest(self):
        try: 
            requests.get('https://stackoverflow.com', timeout=5)
            self.statusLabel.config(text='ONLINE', foreground='green')
        except: 
            self.statusLabel.config(text='OFFLINE', foreground='red')
        self.after_ID = self.after(2000, self.getRequest)
        
class Socket(WorkWindow):
    def __init__(self):
        super().__init__('Socket Method') 
        self.getSocket()
         
    def getSocket(self):
        try: 
            host = socket.gethostbyname("www.stackoverflow.com")
            s = socket.create_connection((host, 80), 5)
            s.close()
            self.statusLabel.config(text='ONLINE', foreground='green')
        except: 
            self.statusLabel.config(text='OFFLINE', foreground='red')
        self.after_ID = self.after(2000, self.getSocket)

if __name__ == '__main__':
    app = TitleWindow()
    app.run()
    
    