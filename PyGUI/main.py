from tkinter import *  


root = Tk() # main window 
root.geometry("300x400") #size of window (width x height)
root.configure(background = "black") #background color
'''
entrada = Entry(root,
                width = 50, 
                )
entrada.insert(0, "Type your name:")
entrada.pack()
'''

def buttonStart():
    label = Label(root, text = 'Wenas')
    label.pack()
    
#Main steps to using tkinter: 
#1. Create the main widget (root/window)
#2. Create the (other) widgets 
#3. Pack the widgets into the window
#4. Enter the main loop


#mylabel = Label(root, text = "Hello App!") #Label widget
#mylabel.pack() #shoving it onto screen
#mylabel.grid(row = 0, column = 0) #Grid system (rows and columns) 
#mylabel = Label(root, text = "Hello world!").grid(row = 0, column = 0) 

label = Label(root, 
              text = 'Welcome to the TIC TAC TOE game!',
              font = ('Courier', 10), 
              fg = 'white', 
              bg = 'black'
              )
label.pack()

startbutton = Button(root, 
                        text = 'Start Game',
                        padx = 50, 
                        pady = 20, 
                        fg = "white", 
                        bg = "green"
                        ) #command = "Que lleve a la otra pantalla"
startbutton.pack(
            expand = True,
            ipadx = 8,
            ipady = 3,
            padx = 60,
            pady = 20,
            fill = 'y'
)

scorebutton = Button(root, 
                        text = 'Show Score',
                        padx = 50, 
                        pady = 20, 
                        fg = "white", 
                        bg = "#560BAC"
                        ) #command = "Que lleve a la otra pantalla"
scorebutton.pack(
            expand = True,
            fill = 'y',
            ipadx = 8,
            ipady = 3,
            padx = 60,
            pady = 20
)  



root.mainloop() #keeps the window open (and refreshes it)