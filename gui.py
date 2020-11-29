from tkinter import *


def screen():


	def message(working = False):
		window = Tk()
		if working:
			Label(window,text='Password Success!').pack()
		else:
			Label(window,text='Invalid Password!').pack()
			
		Button(window,text='OK',command=window.destroy).pack()
		
		window.mainloop()
	
	def click():
		if e.get() == 'password':
			message(working = True)
		else:
			message()
			


	root = Tk()

	root.title('password-prompt')
	root.resizable(0,0)

	root.configure(bg='black')

	Label(root, text='Password:', font=(None,20),bg='black', fg='blue').pack()

	e = Entry(root, borderwidth=10, bg='blue',fg='black',font=(None,13),show='*')
	e.pack()

	Button(root, padx=100, text='Validate',fg='red',command=click).pack()
		

	root.mainloop()

screen()

