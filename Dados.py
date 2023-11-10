import random
import tkinter as tk
from tkinter import messagebox

class DiceRollingGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Jogo de Rolagem de Dados")
        self.master.geometry("300x150")

        self.label = tk.Label(self.master, text="Informe o número de vezes que deseja lançar os dados:")
        self.label.pack(pady=10)

        self.entry = tk.Entry(self.master)
        self.entry.pack(pady=5)

        self.button = tk.Button(self.master, text="Lançar Dados", command=self.simular_rolagem)
        self.button.pack(pady=10)

        self.results_label = tk.Label(self.master, text="")
        self.results_label.pack()

    def simular_rolagem(self):
        try:
            entrada = self.entry.get()
            if entrada.isdigit():
                n = int(entrada)

                frequencias = [0] * 11

                for _ in range(n):
                    dado1 = random.randint(1, 6)
                    dado2 = random.randint(1, 6)
                    soma = dado1 + dado2
                    frequencias[soma - 2] += 1

                # Format the results for display
                results_text = "\nResultados:"
                for soma, frequencia in enumerate(frequencias, start=2):
                    results_text += f'\nGanho {soma}: {frequencia} vezes'

                self.results_label.config(text=results_text)

            else:
                messagebox.showerror("Erro", "Digite um número válido para a simulação.")

        except ValueError:
            messagebox.showerror("Erro", "Digite um número válido para a simulação.")

if __name__ == "__main__":
    root = tk.Tk()
    app = DiceRollingGame(root)
    root.mainloop()

