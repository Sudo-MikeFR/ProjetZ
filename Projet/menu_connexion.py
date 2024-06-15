import tkinter as tk
from tkinter import messagebox
from Classes import exemple_employe
from menu_principal import MenuPrincipal


class LoginWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Connexion")

        # Nom d'utilisateur
        self.label_username = tk.Label(master, text="Nom d'utilisateur")
        self.label_username.grid(row=0, column=0)
        self.entry_username = tk.Entry(master)
        self.entry_username.grid(row=0, column=1)

        # Mot de passe
        self.label_password = tk.Label(master, text="Mot de passe")
        self.label_password.grid(row=1, column=0)
        self.entry_password = tk.Entry(master, show="*")
        self.entry_password.grid(row=1, column=1)

        # Bouton de connexion
        self.button_login = tk.Button(master, text="Connexion", command=self.validate_login)
        self.button_login.grid(row=2, column=1)

        # Bouton quitter
        self.button_quit = tk.Button(master, text="Quitter", command=self.master.quit)
        self.button_quit.grid(row=2, column=0)

    def validate_login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        if not username or not password:
            messagebox.showerror("Erreur", "Veuillez entrer un nom d'utilisateur et un mot de passe.")
            return

        for employe in exemple_employe:
            if employe.username == username and employe.password == password:
                messagebox.showinfo("Succès", f"Bienvenue, {employe.prenom}!")
                self.open_menu_principal(employe)
                return

        messagebox.showerror("Erreur", "Nom d'utilisateur ou mot de passe incorrect.")

    def open_menu_principal(self, employe):
        self.master.withdraw()  # Masquer la fenêtre de connexion
        self.new_window = tk.Toplevel(self.master)
        self.app = MenuPrincipal(self.new_window, self.master, employe)


if __name__ == "__main__":
    root = tk.Tk()
    login_window = LoginWindow(root)
    root.mainloop()
