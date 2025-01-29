import tkinter as tk
from tkinter import messagebox
import requests

def get_address():
    cep = entry_cep.get()
    if len(cep) != 8:
        messagebox.showerror("Erro", "CEP deve ter 8 dígitos.")
        return

    url = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if "erro" in data:
            messagebox.showerror("Erro", "CEP não encontrado.")
        else:
            address = f"{data['logradouro']}, {data['bairro']}, {data['localidade']} - {data['uf']}"
            label_address.config(text=address)
    else:
        messagebox.showerror("Erro", "Falha ao obter o endereço.")

# Cria a janela principal
root = tk.Tk()
root.title("Consulta de CEP")
root.configure(bg="green")
root.geometry("600x300")
root.resizable(True, True)

# Cria os widgets
label_cep = tk.Label(root, text="Digite o CEP:", bg="black", fg="yellow")
entry_cep = tk.Entry(root, bg="black", fg="yellow", insertbackground="yellow")
button_consultar = tk.Button(root, text="Consultar", command=get_address, bg="black", fg="yellow")
label_localizacao = tk.Label(root, text="Localização:", bg="black", fg="yellow")
label_address = tk.Label(root, text="", wraplength=300, justify="left", bg="black", fg="yellow")

# Posiciona os widgets na janela
label_cep.pack(pady=5)
entry_cep.pack(pady=5)
button_consultar.pack(pady=5)
label_localizacao.pack(pady=5)
label_address.pack(pady=5)

# Inicia o loop principal da aplicação
root.mainloop()