import tkinter as tk
from tkinter import ttk, messagebox  # Importer messagebox pour la confirmation
from Classes import clients


class MenuGestion:
    def __init__(self, master, menu_principal):
        self.master = master
        self.menu_principal = menu_principal
        self.master.title("Gestion des Utilisateurs")

        # Titre de la fenêtre
        self.label_title = tk.Label(master, text="Gestion des Utilisateurs")
        self.label_title.pack()

        # Tableau des utilisateurs
        self.tableau = tk.Frame(master)
        self.tableau.pack()

        self.columns = ("Nom", "Prénom", "Courriel")
        self.tree = ttk.Treeview(self.tableau, columns=self.columns, show='headings')

        for col in self.columns:
            self.tree.heading(col, text=col)

        for client in clients:
            self.tree.insert("", tk.END, values=(client.nom, client.prenom, client.courriel))

        self.tree.pack()

        # Boutons
        self.button_creer = tk.Button(master, text="Créer", command=self.creer)
        self.button_creer.pack(side=tk.LEFT, padx=10, pady=10)

        self.button_modifier = tk.Button(master, text="Modifier", command=self.modifier)
        self.button_modifier.pack(side=tk.LEFT, padx=10, pady=10)

        self.button_supprimer = tk.Button(master, text="Supprimer", command=self.supprimer)
        self.button_supprimer.pack(side=tk.LEFT, padx=10, pady=10)

        self.button_retour = tk.Button(master, text="Retour", command=self.retour)
        self.button_retour.pack(side=tk.RIGHT, padx=10, pady=10)

    def creer(self):
        print("bravo")

    def modifier(self):
        print("bravo")

    def supprimer(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Avertissement", "Veuillez sélectionner un utilisateur à supprimer.")
            return
        utilisateur = self.tree.item(selected_item, "values")
        reponse = messagebox.askyesno("Confirmation",
                                      f"Voulez-vous vraiment supprimer {utilisateur[0]} {utilisateur[1]}?")
        if reponse:
            self.tree.delete(selected_item)
            print(f"Utilisateur {utilisateur[0]} {utilisateur[1]} supprimé.")

    def retour(self):
        self.master.destroy()
        self.menu_principal.master.deiconify()  # Réafficher la fenêtre principale


if __name__ == "__main__":
    root = tk.Tk()
    app = MenuGestion(root, None)
    root.mainloop()
