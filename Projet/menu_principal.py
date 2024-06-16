import tkinter as tk
from menu_films import MenuFilms
from menu_gestion import MenuGestion
from Menu_Quitter import menuquitter
### ici c'est la fênetre principale , c'est un menu qui ouvre d'autre menu simplement, dans ce menu nous validons aussi si
#l'utilisateur est en lecture ou en modifie

## Disposition des menus
class MenuPrincipal:
    def __init__(self, master, login_window, employe):
        self.master = master
        self.login_window = login_window
        self.employe = employe
        self.master.title("Menu Principal")

        # Bouton Gérer les utilisateurs
        self.button_gerer_utilisateurs = tk.Button(master, text="Gérer les utilisateurs",
                                                   command=self.gerer_utilisateurs)
        self.button_gerer_utilisateurs.grid(row=0, column=0)

        # Désactiver le bouton si l'employé a un accès de type "lecture"
        if self.employe.type_acces == "lecture":
            ## disable pour le griser
            self.button_gerer_utilisateurs.config(state=tk.DISABLED)

        # Bouton Voir les films
        self.button_voir_films = tk.Button(master, text="Voir les films", command=self.voir_films)
        self.button_voir_films.grid(row=0, column=1)

        # Bouton Déconnexion
        self.button_deconnexion = tk.Button(master, text="Déconnexion", command=self.deconnexion)
        self.button_deconnexion.grid(row=1, column=0)

        # Bouton Quitter
        self.button_quit = tk.Button(master, text="Quitter", command=self.master.quit)
        self.button_quit.grid(row=1, column=1)
    ##Donc plus bas, c'est les defs pour ouvrir les différents menus
    def gerer_utilisateurs(self):
        new_window = tk.Toplevel(self.master)
        self.app = MenuGestion(new_window, self)
        self.master.withdraw()  # Masquer la fenêtre actuelle
    def voir_films(self):
        new_window = tk.Toplevel(self.master)
        self.app = MenuFilms(new_window, self)
        self.master.withdraw()  # Masquer la fenêtre actuelle
    def deconnexion(self):
        self.master.destroy()
        self.login_window.deiconify()  # Réafficher la fenêtre de connexion


if __name__ == "__main__":
    root = tk.Tk()
    app = MenuPrincipal(root, None, None)
    root.mainloop()
