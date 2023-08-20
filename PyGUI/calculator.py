from tkinter import *

root = Tk()
root.title('Calculator')
root.geometry("330x440")
root.configure(background = 'black')
root.resizable(False,False)

#ipadding = {'ipadx': 10, 'ipady': 10}

#root.rowconfigure(0, weight = 4)
#root.columnconfigure(0, weight = 2)

#Entry bar
frame1 = Frame(root)
entrybar = Label(frame1,
                 height = 3,
                 width = 46,
                 justify = RIGHT,
                 anchor = NE,
                 pady = 6,
                 padx = 3,
                 text = 'alo',#show numbers & results
                )
entrybar.pack()

'''
frame_keyb = Frame(root)
frame_2 = Frame(frame_keyb)
frame_3 = Frame(frame_keyb)
frame_4 = Frame(frame_keyb)
frame_5 = Frame(frame_keyb)
'''

Nbuttons = []
Opbuttons = []
#Buttons (numbers 0-9)
numbers = [i for i in range(0,10)]
for i in numbers:
    i = Button(root, 
                    text = i, 
                    bg = 'white',
                    fg = 'blue',
                    padx = 25,
                    pady = 25
                    #command                 
                    )
    Nbuttons.append(i)    

#Operators (+,-,*,/,=)
operators = ['+', '-', 'x', '%', 'C', '=']
for i in operators:
    i = Button(root, 
                    text = i, 
                    bg = 'white',
                    fg = 'green', 
                    #command 
                    )
    Opbuttons.append(i)

#Nbuttons[0].grid(row = 1, column = 0, sticky = NW) 

frame1.pack()
#frame_keyb.pack()


root.mainloop()
