from tkinter import *

def Calculadora(object):
    def __init__(self,i):

        #coloca a entrada de texto
        self.form = Entry(i)
        self.form.pack()

        #botao calcular
        self.calc = Button(i,text="Calcule",command=Calcular)
        self.calc.pack()

        #texto das formulas
        self.resultado = Label(i,text="Resultado",fg="blue")
        self.resultado.pack()

        botoes = ('comb(n,k)','binominal(n,x,p)','poisson(l,x,t)','soma(n,p,maior,menor=0)','media','desvio','moda','mediana',
'variancia','p(x>k)','p(x>=k)','p(x<k)','p(x<=k)','p(k1<x<k2)','p(k1<=x<k2)','p(k1<x<=k2)','p(k1<=x<=k2)')

        for b in botoes:
            a = Button(i,text=b,bg="green")
            a.pack()

    def Calcular(self):
        self.resultado['text'] = self.form.get()
        self.resultado['fg'] = 'green'

#cria a nossa tela
i = Tk()

Calculadora(i)

#da um titulo a instancia
i.title('Calculadora Cientifica')

#da um tamanha da tela
i.geometry("800x600")

#da um icone ao aplicativo
#i.wm_iconbitmap('icone.ico')

i.mainloop()