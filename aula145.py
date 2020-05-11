from tkinter import*

i = Tk()

i.title("Brincando")

i.geometry("400x300")

texto = Label(i,text="Meu Texto")
texto.pack()

b = Button(i,text="Clique!")
b.pack()

i.mainloop()
