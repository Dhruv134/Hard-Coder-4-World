from tkinter import *
from tkinter import messagebox as mb

LargeFont = 'Lato 18 bold'
NormalFont = 'Lato 12'
ButtonFont = 'Lato 12 bold'


root = Tk()

root.geometry("500x480")
root.configure(bg="#263D42")

def loginGUI(preFrame=None):

	preFrame = Frame(root,bg='#263D42')
	preFrame.place(in_=root, anchor='c', relx=0.5, rely=0.5)

	h1 = Label(preFrame, text='Login page', bg="#263D42", fg="#ffffff", font=LargeFont)
	h1.grid(row=0, column=0, columnspan=2)

	blank = Label(preFrame, text='', bg="#263D42", fg="#ffffff", font=NormalFont)
	blank.grid(row=1, column=0)

	l1 = Label(preFrame, text='User Id : ', bg="#263D42", fg="#ffffff", font=NormalFont)
	l1.grid(row=2, column=0 )

	uid = Entry(preFrame, fg="#263D42", font=NormalFont)
	uid.grid(row=2, column=1 )

	l2 = Label(preFrame, text="Password : ", bg="#263D42", fg="#ffffff", font=NormalFont)
	l2.grid(row=3, column=0)

	password = Entry(preFrame, show='*', fg="#263D42", font=NormalFont)
	password.grid(row=3, column=1 )

	blank = Label(preFrame, text='', bg="#263D42", fg="#ffffff", font=NormalFont)
	blank.grid(row=4, column=0)

	submit = Button(preFrame, text='Submit', fg="#263D42", font=ButtonFont)
	submit.grid(row=5, column=0, columnspan=2)

loginGUI()

root.mainloop()
