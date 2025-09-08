import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # Necesario para .jpg o imágenes más grandes

def wish_good_luck():
    messagebox.showinfo("Que terca eres", "En fin, confía en ti y disfrutalo! 💃✨")

# Crear ventana
root = tk.Tk()
root.title("GL on it 🎶")
root.geometry("420x420")  # un poco más grande para la imagen
root.config(bg="#1c1c1c")

# Cargar imagen (asegúrate de tener un archivo "colmillito.png" en la misma carpeta)
try:
    img = Image.open("colmillito.png")  # puedes usar .jpg o .png
    img = img.resize((150, 150))  # ajustar tamaño
    photo = ImageTk.PhotoImage(img)

    img_label = tk.Label(root, image=photo, bg="#1c1c1c")
    img_label.image = photo  # evitar que lo borre el recolector de basura
    img_label.pack(pady=10)
except:
    fallback = tk.Label(root, text="(imagen no encontrada)", fg="gray", bg="#1c1c1c")
    fallback.pack()

# Mensaje principal
label = tk.Label(
    root,
    text="Vamos Kris! 🎶\n\nCon 'COLMILLO' la vas a romper grr 🫦🔥",
    font=("Arial", 12, "bold"),
    fg="white",
    bg="#1c1c1c",
    wraplength=350,
    justify="center"
)
label.pack(pady=10)

# Botón motivador
btn = tk.Button(
    root,
    text="No presionar",
    font=("Arial", 12, "bold"),
    bg="#ff5c8a",
    fg="white",
    command=wish_good_luck
)
btn.pack(pady=20)

# Ejecutar ventana
root.mainloop()
