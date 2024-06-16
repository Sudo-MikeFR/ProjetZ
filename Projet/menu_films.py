import tkinter as tk
from Classes import films
from Menu_Quitter import menuquitter

###ici c'est le menu qui contient les  films
## disposition de la fenetre
class MenuFilms:
    def __init__(self, master, menu_principal):
        self.master = master
        self.menu_principal = menu_principal
        self.master.title("Liste des Films")

        # Titre de la fenêtre
        self.label_title = tk.Label(master, text="Liste des Films")
        self.label_title.pack()

        # Liste des films , les afficher dans le menu / listbox
        self.listbox_films = tk.Listbox(master)
        for film in films:
            self.listbox_films.insert(tk.END, film.nom_film)
        self.listbox_films.pack()

        # Lorsqu'on double clique, faire l'action afficher_details_film (def plus bas)
        self.listbox_films.bind('<Double-1>', self.afficher_details_film)

        # Bouton Retour
        self.button_retour = tk.Button(master, text="Retour", command=self.retour)
        self.button_retour.pack()

    def afficher_details_film(self, event):
        # Obtenir le film sélectionné
        ## creation de la selection , donc quand je clique sur un film , selectionne le
        index_selectionne = self.listbox_films.curselection()
        ## met le films selectionné dans la [] , afficher les détails
        if index_selectionne:
            film_selectionne = films[index_selectionne[0]]
            ##création du détails, avec la façon dont ont veut la fenetre,
            details = (
                f"Nom: {film_selectionne.nom_film}\n"
                f"Durée: {film_selectionne.duree_film}\n"
                f"Description: {film_selectionne.description_film}\n"
                f"Catégories: {', '.join(cat.nom_categorie for cat in film_selectionne.categories)}\n"
                f"Acteurs: {', '.join(f'{acteur.prenom} {acteur.nom}' for acteur in film_selectionne.acteur)}"
            )
            #le faire afficher (details plus haut avec les dispositions plus bas)
            self.afficher_fenetre_details(details)

            ###Dispositions de la fenetre demandé juste en haut
    def afficher_fenetre_details(self, details):
        ## creation de la nouvelle fenetre pour afficher les détails
        fenetre_details = tk.Toplevel(self.master)
        fenetre_details.title("Détails du Film")
        label_details = tk.Label(fenetre_details, text=details, justify=tk.LEFT)
        label_details.pack(padx=10, pady=10)
        ###bouton fermer pour cette fenetre de détails
        bouton_fermer = tk.Button(fenetre_details, text="Fermer", command=fenetre_details.destroy)
        bouton_fermer.pack(pady=5)
### bouton retour
    def retour(self):
        self.master.destroy()
        self.menu_principal.master.deiconify()  # Réafficher la fenêtre principale


if __name__ == "__main__":
    root = tk.Tk()
    app = MenuFilms(root, None)
    root.mainloop()
