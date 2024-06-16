#Partir le code ici, ouvre le Menu_Connexion

import tkinter as tk
from menu_connexion import LoginWindow

if __name__ == "__main__":
    root = tk.Tk()
    login_window = LoginWindow(root)
    root.mainloop()
