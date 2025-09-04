import tkinter as tk
ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("400x400")

etiqueta = tk.Label(ventana, text="Ingresa un numero")
etiqueta.pack(pady = 5)

etiqueta2 = tk.Label(ventana, text="Ingresa otro numero")
etiqueta2.pack(pady = 5)

entrada = tk.Entry(ventana)
entrada.pack(pady = 5)
entrada2 = tk.Entry(ventana)
entrada2.pack(pady = 5)

def sumar():
    numero1 = int(entrada.get())
    numero2 = int(entrada2.get())
    resultado = numero1 + numero2
    etiqueta.config(text=resultado)
def restar():
    numero1 = int(entrada.get())
    numero2 = int(entrada2.get())
    resultado = numero1 - numero2
    etiqueta.config(text=resultado)
def multiplicar():
    numero1 = int(entrada.get())
    numero2 = int(entrada2.get())
    resultado = numero1 * numero2
    etiqueta.config(text=resultado)
def dividir():
    numero1 = int(entrada.get())
    numero2 = int(entrada2.get())
    resultado = numero1 / numero2
    etiqueta.config(text=resultado)

boton_multiplicar = tk.Button(ventana, text="Multiplicar", command=multiplicar)
boton_multiplicar.pack(pady = 5)
boton_dividir = tk.Button(ventana, text="Dividir", command=dividir)
boton_dividir.pack(pady = 1)
boton_restar = tk.Button(ventana, text="Restar", command=restar)
boton_restar.pack(pady = 5)
boton_sumar = tk.Button(ventana, text="Sumar", command=sumar)
boton_sumar.pack(pady = 5)
ventana.mainloop()
#para entenderlo lo hice con funciones, ahora lo hare con metodos
