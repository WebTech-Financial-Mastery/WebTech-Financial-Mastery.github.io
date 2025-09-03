import win32print
import tkinter as tk
from tkinter import messagebox, ttk

# Obtener todas las impresoras instaladas
impresoras = [printer[2] for printer in win32print.EnumPrinters(2)]

def imprimir_prueba():
    seleccion = combo.get()
    if not seleccion:
        messagebox.showwarning("Aviso", "Selecciona una impresora")
        return
    try:
        # Configuramos la impresora seleccionada
        handle = win32print.OpenPrinter(seleccion)
        job = win32print.StartDocPrinter(handle, 1, ("Prueba de Impresión", None, "RAW"))
        win32print.StartPagePrinter(handle)
        win32print.WritePrinter(handle, b"Esto es una prueba de impresión\n")
        win32print.EndPagePrinter(handle)
        win32print.EndDocPrinter(handle)
        win32print.ClosePrinter(handle)
        messagebox.showinfo("Éxito", f"Se envió prueba a '{seleccion}'")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# GUI simple
root = tk.Tk()
root.title("Seleccionar Impresora - Test")

tk.Label(root, text="Elige la impresora para probar:").pack(pady=10)
combo = ttk.Combobox(root, values=impresoras, width=40)
combo.pack(pady=5)
tk.Button(root, text="Imprimir Prueba", command=imprimir_prueba).pack(pady=20)

root.mainloop()
