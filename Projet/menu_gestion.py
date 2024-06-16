import tkinter as tk
from tkinter import messagebox, ttk
from Classes import clients
from menu_creation import MenuCreation
from menu_modification import MenuModification
from menu_cartes import MenuCartes

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

        self.columns = ("Nom", "Prénom", "Courriel", "Cartes de Crédit")
        self.tree = ttk.Treeview(self.tableau, columns=self.columns, show='headings')

        for col in self.columns:
            self.tree.heading(col, text=col)

        self.update_tree()

        self.tree.pack()

        # Boutons
        self.button_creer = tk.Button(master, text="Créer", command=self.creer)
        self.button_creer.pack(side=tk.LEFT, padx=10, pady=10)

        self.button_modifier = tk.Button(master, text="Modifier", command=self.modifier)
        self.button_modifier.pack(side=tk.LEFT, padx=10, pady=10)

        self.button_supprimer = tk.Button(master, text="Supprimer", command=self.supprimer)
        self.button_supprimer.pack(side=tk.LEFT, padx=10, pady=10)

        self.button_ajouter_carte = tk.Button(master, text="Ajouter Carte", command=self.ajouter_carte)
        self.button_ajouter_carte.pack(side=tk.LEFT, padx=10, pady=10)

        self.button_retirer_carte = tk.Button(master, text="Retirer Carte", command=self.retirer_carte)
        self.button_retirer_carte.pack(side=tk.LEFT, padx=10, pady=10)

        self.button_retour = tk.Button(master, text="Retour", command=self.retour)
        self.button_retour.pack(side=tk.RIGHT, padx=10, pady=10)

    def update_tree(self):
        for i in self.tree.get_children():
            self.tree.delete(i)

        for client in clients:
            cartes = ", ".join([f"{carte.numero} (exp: {carte.date_expire})" for carte in client.cartes_credit])
            self.tree.insert("", tk.END, values=(client.nom, client.prenom, client.courriel, cartes))

    def creer(self):
        new_window = tk.Toplevel(self.master)
        self.app = MenuCreation(new_window, self)

    def modifier(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Avertissement", "Veuillez sélectionner un utilisateur à modifier.")
            return

        utilisateur = self.tree.item(selected_item[0], "values")
        courriel = utilisateur[2]

        # Trouver le client correspondant au courriel
        client = None
        for c in clients:
            if c.courriel == courriel:
                client = c
                break

        if client:
            new_window = tk.Toplevel(self.master)
            self.app = MenuModification(new_window, self, client)
        else:
            messagebox.showerror("Erreur", "Utilisateur non trouvé.")

    def supprimer(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Avertissement", "Veuillez sélectionner un utilisateur à supprimer.")
            return
        utilisateur = self.tree.item(selected_item, "values")
        reponse = messagebox.askyesno("Confirmation", f"Voulez-vous vraiment supprimer {utilisateur[0]} {utilisateur[1]}?")
        if reponse:
            # Supprimer de la Treeview
            self.tree.delete(selected_item)

            # Supprimer de la liste des clients dans la classe
            for client in clients[:]:
                if client.nom == utilisateur[0] and client.prenom == utilisateur[1] and client.courriel == utilisateur[2]:
                    clients.remove(client)
                    print(f"Utilisateur {client.nom} {client.prenom} supprimé de la liste des clients.")
                    break

    def ajouter_carte(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Avertissement", "Veuillez sélectionner un utilisateur.")
            return

        utilisateur = self.tree.item(selected_item[0], "values")
        courriel = utilisateur[2]

        # Trouver le client correspondant au courriel
        client = None
        for c in clients:
            if c.courriel == courriel:
                client = c
                break

        if client:
            new_window = tk.Toplevel(self.master)
            self.app = MenuCartes(new_window, client, action="ajouter", menu_gestion=self)
        else:
            messagebox.showerror("Erreur", "Utilisateur non trouvé.")

    def retirer_carte(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Avertissement", "Veuillez sélectionner un utilisateur.")
            return

        utilisateur = self.tree.item(selected_item[0], "values")
        courriel = utilisateur[2]

        # Trouver le client correspondant au courriel
        client = None
        for c in clients:
            if c.courriel == courriel:
                client = c
                break

        if client:
            new_window = tk.Toplevel(self.master)
            self.app = MenuCartes(new_window, client, action="retirer", menu_gestion=self)
        else:
            messagebox.showerror("Erreur", "Utilisateur non trouvé.")

    def retour(self):
        self.master.destroy()
        self.menu_principal.master.deiconify()  # Réafficher la fenêtre principale


if __name__ == "__main__":
    root = tk.Tk()
    app = MenuGestion(root, None)
    root.mainloop()
