import os
import tkinter as tk
from tkinter import filedialog, messagebox, Toplevel
import win32print
import win32api

def select_file():
    global selected_file_path
    file_path = filedialog.askopenfilename(filetypes=[("Documentos", "*.docx *.xlsx *.pdf *.btw")])
    if file_path:
        selected_file_path = file_path
        selected_file_label.config(text=f"Arquivo selecionado: {os.path.basename(file_path)}")
    else:
        selected_file_path = None
        selected_file_label.config(text="Nenhum arquivo selecionado")

def show_options_window():
    options_window = Toplevel(root)
    options_window.title("Mais Opções")
    options_window.geometry("300x200")

    label_style = {'font': ('Arial', 12), 'pady': 5}
    entry_style = {'font': ('Arial', 12), 'width': 20}

    width_label = tk.Label(options_window, text="Largura (cm):", **label_style)
    width_label.pack(pady=5)
    width_entry = tk.Entry(options_window, **entry_style)
    width_entry.pack(pady=5)

    height_label = tk.Label(options_window, text="Altura (cm):", **label_style)
    height_label.pack(pady=5)
    height_entry = tk.Entry(options_window, **entry_style)
    height_entry.pack(pady=5)

    def save_options():
        global width, height
        try:
            width = float(width_entry.get())
            height = float(height_entry.get())
            if width <= 0 or height <= 0:
                raise ValueError("Largura e altura devem ser valores positivos.")
            options_window.destroy()
        except ValueError as ve:
            messagebox.showerror("Erro", f"Entrada inválida: {ve}")

    save_button = tk.Button(options_window, text="Salvar", command=save_options, font=('Arial', 12))
    save_button.pack(pady=20)

def print_file():
    if not selected_file_path:
        messagebox.showerror("Erro", "Nenhum arquivo selecionado.")
        return

    try:
        num_copies = int(copies_entry.get())
        if num_copies < 1:
            raise ValueError("O número de cópias deve ser pelo menos 1.")
        
        if 'width' in globals() and 'height' in globals():
            print(f"Imprimindo com largura: {width} cm e altura: {height} cm")
        else:
            width = height = None

        for _ in range(num_copies):
            win32api.ShellExecute(0, "print", selected_file_path, None, ".", 0)
        
        messagebox.showinfo("Sucesso", f"{num_copies} cópias enviadas para impressão." +
                            (f"\nTamanho: {width} x {height} cm" if width and height else ""))
    except ValueError as ve:
        messagebox.showerror("Erro", f"Entrada inválida: {ve}")

selected_file_path = None

root = tk.Tk()
root.title("Gerenciador de Impressão")

root.geometry("500x300")

label_style = {'font': ('Arial', 12), 'pady': 5}
entry_style = {'font': ('Arial', 12), 'width': 30}

select_button = tk.Button(root, text="Selecionar Arquivo", command=select_file, font=('Arial', 12))
select_button.pack(pady=20)

selected_file_label = tk.Label(root, text="Nenhum arquivo selecionado", **label_style)
selected_file_label.pack(pady=5)

copies_label = tk.Label(root, text="Número de cópias:", **label_style)
copies_label.pack(pady=5)
copies_entry = tk.Entry(root, **entry_style)
copies_entry.pack(pady=5)

print_button = tk.Button(root, text="Imprimir Arquivo", command=print_file, font=('Arial', 12))
print_button.pack(pady=20)

more_options_button = tk.Button(root, text="Mais Opções", command=show_options_window, font=('Arial', 12))
more_options_button.pack(pady=10)

root.mainloop()
