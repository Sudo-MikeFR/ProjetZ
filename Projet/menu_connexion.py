import tkinter as tk
from tkinter import messagebox
from Classes import exemple_employe
from menu_principal import MenuPrincipal
from Menu_Quitter import menuquitter

####MENU POUR LA CONNEXION, Prends les informations de connexion de employe, s'assure que c'est le bon.
#Compte : admin/admin ou test/test  Admin = Modifie , Test = Lecture, Les menus ne seront pas les mêmes pour les deux utilisateurs


## Disposition de la fenetre
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
        ## ici pour cache le mot de passe : show="*"
        self.entry_password = tk.Entry(master, show="*")
        self.entry_password.grid(row=1, column=1)

        # Bouton de connexion
        self.button_login = tk.Button(master, text="Connexion", command=self.validate_login)
        self.button_login.grid(row=2, column=1)

        # Bouton quitter
        self.button_quit = tk.Button(master, text="Quitter", command=self.master.quit)
        self.button_quit.grid(row=2, column=0)
### ici c'est pour la validation des entrées
    def validate_login(self):
        ## l'utilisateur entre les identifiants et les mets dans username and password
        username = self.entry_username.get()
        password = self.entry_password.get()
## si aucune entrée n'est mis : donc si rien =
        if not username or not password:
            messagebox.showerror("Erreur", "Veuillez entrer un nom d'utilisateur et un mot de passe.")
            return
            ### si username == au username de l'employe et la même chose pour le mot de passe. Ouvre le menu principal
        for employe in exemple_employe:
            if employe.username == username and employe.password == password:
                self.open_menu_principal(employe)
                return
#### sinon , tu retourne le message d'erreur
        messagebox.showerror("Erreur", "Nom d'utilisateur ou mot de passe incorrect.")
    ## pour ouvrir la fenetre menu_principal quand l'utilisateur entre un bon code d'acces
    def open_menu_principal(self, employe):
        self.master.withdraw()  # Masquer la fenêtre de connexion
        self.new_window = tk.Toplevel(self.master)
        self.app = MenuPrincipal(self.new_window, self.master, employe)


if __name__ == "__main__":
    root = tk.Tk()
    login_window = LoginWindow(root)
    root.mainloop()
