import tkinter as tk
import math

 # configuração dos botões
botao_config = {
    "bg": "#343d59",
    "fg": "#f2efbd",
    "font": ("Cooper Black", 14),
    "height": "2",
    "width": "7",
    "relief": "flat",
    "activebackground": "#26a682"
    }

 #botões especiais para tratamentos diferentes
especiais = ["x²", "C", "n!"]

class Calculadora:
    def __init__(self, janela):

        self.janela = janela

        self.visorFrame = tk.Frame(self.janela)
        self.visorFrame.pack()

        self.buttonsFrame = tk.Frame(self.janela)
        self.buttonsFrame.pack()

        self.output = tk.Entry(self.visorFrame,
                               width = 26, relief = "sunken", bd = 6, font = ("Cooper Black", 19), fg = "#343d59",
                               bg = "#FCE196")
        self.output.grid(row = 0, column = 0)

        self.criarBotoes()

 #criação dos botões para a calculadora
    def criarBotoes(self):
        self.botoes = [
            ["n!", "x²", "**", "/"],
            ["7", "8", "9", "+"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "*"],
            [".", "0", "=", "C"]
            ]

        for linha in range(len(self.botoes)):
            for coluna in range(len(self.botoes[linha])):
                texto = self.botoes[linha] [coluna]
                b = tk.Button(self.buttonsFrame, botao_config, text = texto,
                              command = lambda x = texto : self.acaoBotoes(x))
                b.grid(row = linha, column = coluna)

 #funcionalidades dos botões
    def acaoBotoes(self, texto):
        if texto != "=":
            if texto not in especiais:
                self.output.insert('end', texto)
            else:
                if texto == "x²":
                    self.addValor(float(self.output.get()) ** 2)
                elif texto == "n!":
                    self.addValor(math.factorial(float(self.output.get())))
                elif texto == "C":
                    self.addValor("")
        else:
            self.addValor(eval(self.output.get()))

    def addValor(self, valor):
        self.output.delete(0, "end")
        self.output.insert('end',valor)

raiz = tk.Tk()
Calculadora(raiz)
raiz.mainloop()
