import tkinter as tk

def Calcular():
    num1 = int(entrada1.get())
    num2 = int(entrada2.get())
    escolha = calc.get()
    if escolha == 1:
        resultado = num1 + num2
    elif escolha == 2:
        resultado = num1 - num2
    elif escolha == 3:
        resultado = num1 * num2
    elif escolha == 4:
        if num2 == 0:
            resultado = "Impossível dividir por zero"
        else:
            resultado = num1 / num2
    else:
        resultado = "Erro!!!!!! Seleciona alguma opção né oh lerdão"
    
    lbl_resultado.config(text="Resultado: " + str(resultado))

janela = tk.Tk()
janela.title("Calculadora")
janela.configure(bg='black')

titulo = tk.Label(janela, text="Minha Calculadora", bg='black', fg='red')
titulo.pack()

lbl_entrada1 = tk.Label(janela, text="Primeiro número:", bg='black', fg='white')
lbl_entrada1.pack()
entrada1 = tk.Entry(janela, bg='black', fg='white')
entrada1.pack()

lbl_entrada2 = tk.Label(janela, text="Segundo número:", bg='black', fg='white')
lbl_entrada2.pack()
entrada2 = tk.Entry(janela, bg='black', fg='white')
entrada2.pack()

calc = tk.IntVar()

radio1 = tk.Radiobutton(janela, text="Soma", variable=calc, value=1, bg='black', fg='white', selectcolor='red')
radio1.pack()
radio2 = tk.Radiobutton(janela, text="Subtração", variable=calc, value=2, bg='black', fg='white', selectcolor='red')
radio2.pack()
radio3 = tk.Radiobutton(janela, text="Multiplicação", variable=calc, value=3, bg='black', fg='white', selectcolor='red')
radio3.pack()
radio4 = tk.Radiobutton(janela, text="Divisão", variable=calc, value=4, bg='black', fg='white', selectcolor='red')
radio4.pack()

botao = tk.Button(janela, text="Calcular", command=Calcular, bg='red', fg='white')
botao.pack()

lbl_resultado = tk.Label(janela, text="Resultado: ", bg='black', fg='white')
lbl_resultado.pack()

janela.geometry("1366x768")
janela.mainloop()
