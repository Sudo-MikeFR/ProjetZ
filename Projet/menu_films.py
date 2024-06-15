import tkinter as tk
from Classes import films


class MenuFilms:
    def __init__(self, master, menu_principal):
        self.master = master
        self.menu_principal = menu_principal
        self.master.title("Liste des Films")

        # Titre de la fenêtre
        self.label_title = tk.Label(master, text="Liste des Films")
        self.label_title.pack()

        # Liste des films
        self.listbox_films = tk.Listbox(master)
        for film in films:
            self.listbox_films.insert(tk.END, film.nom_film)
        self.listbox_films.pack()

        # Associer l'événement de double-clic à la liste des films
        self.listbox_films.bind('<Double-1>', self.afficher_details_film)

        # Bouton Retour
        self.button_retour = tk.Button(master, text="Retour", command=self.retour)
        self.button_retour.pack()

    def afficher_details_film(self, event):
        # Obtenir le film sélectionné
        index_selectionne = self.listbox_films.curselection()
        if index_selectionne:
            film_selectionne = films[index_selectionne[0]]
            details = (
                f"Nom: {film_selectionne.nom_film}\n"
                f"Durée: {film_selectionne.duree_film}\n"
                f"Description: {film_selectionne.description_film}\n"
                f"Catégories: {', '.join(cat.nom_categorie for cat in film_selectionne.categories)}"
            )
            self.afficher_fenetre_details(details)

    def afficher_fenetre_details(self, details):
        fenetre_details = tk.Toplevel(self.master)
        fenetre_details.title("Détails du Film")
        label_details = tk.Label(fenetre_details, text=details, justify=tk.LEFT)
        label_details.pack(padx=10, pady=10)

        bouton_fermer = tk.Button(fenetre_details, text="Fermer", command=fenetre_details.destroy)
        bouton_fermer.pack(pady=5)

    def retour(self):
        self.master.destroy()
        self.menu_principal.master.deiconify()  # Réafficher la fenêtre principale


if __name__ == "__main__":
    root = tk.Tk()
    app = MenuFilms(root, None)
    root.mainloop()
