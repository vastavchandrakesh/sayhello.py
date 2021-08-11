from tkinter import *

mw = Tk()

def say_hello():
    #name = userinput.get()
    greeting = 'hello' + name + '!'
    if name !='':
        text.config(text=greeting)
        userinput.delete(0, END)
    else:
        text.config(text='Enter your name!')

userinput = Entry(mw, width=20, front=('Arial', 18))
userinput.pack(padx=10, pady=10)

my_text = Label(mw, text='Enter your name!', font=('Arial', 14))
my_text.pack(pady=5)

btn = Button(mw, text='Say Hello!', font=('Arial', 12), command=say_hello)
btn.pack(pady=20)


mw.mainloop()
