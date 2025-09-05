import tkinter as tk

class Calculadora:
    def __init__(self,ventana):
        self.ventana = ventana
        self.ventana.title("Calculadora")
        self.ventana.geometry("400x400")

        self.etiqueta_resultado = tk.Label(self.ventana, text = "Restultado: ")
        self.etiqueta_resultado.pack(pady = 5)

        self.etiqueta_num1 = tk.Label(self.ventana, text = "Ingresa un numero")
        self.etiqueta_num1.pack(pady = 5)
        self.entrada1 = tk.Entry(self.ventana)
        self.entrada1.pack(pady = 5)

        self.etiqueta_num2 = tk.Label(self.ventana, text = "Ingresa otro numero")
        self.etiqueta_num2.pack(pady = 5)
        self.entrada2 = tk.Entry(self.ventana)
        self.entrada2.pack(pady = 5)

        tk.Button(self.ventana, text = "Sumar", command = self.sumar).pack(pady = 5)
        tk.Button(self.ventana, text = "Restar", command = self.restar).pack(pady = 5)
        tk.Button(self.ventana, text = "Multiplicar", command = self.multiplicar).pack(pady = 5)
        tk.Button(self.ventana, text = "Dividir", command = self.dividir).pack(pady = 5)
        tk.Button(self.ventana, text = "Eliminar", command = self.limpiar).pack(pady = 5)

    def limpiar(self):
        self.entrada1.delete(0, tk.END)
        self.entrada2.delete(0, tk.END)
        self.etiqueta_resultado.config(text = "Ya se limpio")

    def obtener_numeros(self):
        try:
            num1 = float(self.entrada1.get())
            num2 = float(self.entrada2.get())
            return num1, num2
        except ValueError:
            self.etiqueta_resultado.config(text = "Error")
            return None, None

    def sumar(self):
        num1, num2 = self.obtener_numeros()
        if num1 is not None and num2 is not None:
            resultado = num1 + num2
            self.etiqueta_resultado.config(text = f"Suma: {resultado}")

    def restar(self):
        num1, num2 = self.obtener_numeros()
        if num1 is not None and num2 is not None:
            resultado = num1 - num2
            self.etiqueta_resultado.config(text = f"Resta: {resultado}")

    def multiplicar(self):
        num1, num2 = self.obtener_numeros()
        if num1 is not None and num2 is not None:
            resultado = num1 * num2
            self.etiqueta_resultado.config(text = f"Multiplica: {resultado}")

    def dividir(self):
        num1, num2 = self.obtener_numeros()
        if num1 is not None and num2 is not None:
            if num1 != 0:
                resultado = num1 / num2
                self.etiqueta_resultado.config(text = f"Dividir: {resultado}")
            else: self.etiqueta_resultado.config(text = "No se puede dividir por 0")

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculadora(root)
    root.mainloop()

