import tkinter as tk
from tkinter import messagebox
import random

def ask_why():
    # Neues Fenster erstellen
    root = tk.Tk()
    root.title("Die existenzielle Frage")
    
    # Zufällige Position auf dem Bildschirm
    width = 300
    height = 150
    x = random.randint(0, root.winfo_screenwidth() - width)
    y = random.randint(0, root.winfo_screenheight() - height)
    root.geometry(f"{width}x{height}+{x}+{y}")

    tk.Label(root, text="Aber... warum?", font=("Arial", 12, "bold")).pack(pady=10)
    
    entry = tk.Entry(root, width=30)
    entry.pack(pady=5)
    entry.focus_set()

    def on_submit():
        if entry.get().strip():
            # Erstellt ein neues Fenster, bevor das alte bleibt oder schließt
            ask_why() 
        else:
            messagebox.showwarning("Fehler", "Du musst mir eine Erklärung geben!")

    tk.Button(root, text="Erklären", command=on_submit).pack(pady=10)
    root.mainloop()

if __name__ == "__main__":
    ask_why()
