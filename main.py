from tkinter import *

class UnitConvertor:

    def __init__(self):
        # load initial gui
        self.root = Tk()
        self.load_initial_gui()
        self.root.mainloop()

    def load_initial_gui(self):

        self.root.title('Unit Convertor')
        self.root.geometry('250x350')
        self.root.resizable(0, 0)
        self.root.configure(background='black')

        heading = Label(self.root, text='Unit Convertor', bg='black', fg='white')
        heading.pack(pady=(20, 20))
        heading.config(font=('verdana', 18))

        btn1 = Button(self.root, text='USD to INR', command=self.usd_to_inr)
        btn1.pack()

        btn2 = Button(self.root, text='Miles to Kms')
        btn2.pack()

        btn3 = Button(self.root, text='Kg to Pound')
        btn3.pack()



    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()

    def usd_to_inr(self):

        self.clear()
        label1 = Label(self.root,text='Enter amount in USD',bg='black',fg='white')
        label1.pack(pady=(20,5))
        label1.config(font=('verdana',14))

        self.user_input = Entry(self.root)
        self.user_input.pack()

        btn = Button(self.root,text='Convert',command=self.usd_to_inr_convertor)
        btn.pack()

        self.result = Label(self.root,text='',bg='black',fg='white')
        self.result.pack(pady=(20,20))
        self.result.config(font=('verdana',24))

        back = Button(self.root,text='Back',command=self.go_back)
        back.pack()

    def usd_to_inr_convertor(self):
        # number fetch
        usd = self.user_input.get()
        # convert to inr
        inr = int(usd)*75
        # display
        self.result.config(text=str(inr))


    def go_back(self):
        self.clear()
        self.load_initial_gui()

    def miles_to_km(self):
        self.clear()

    def pound_to_kgs(self):
        self.clear()
        self.load_initial_gui()

# creating an object of Unitconvertor class
obj = UnitConvertor()