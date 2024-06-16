import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from Classes import CarteCredit
from Menu_Quitter import menuquitter



class MenuCartes:
    def __init__(self, master, client, action, menu_gestion):
        # Initialisation des paramètres principaux
        self.master = master
        self.client = client  # Le client auquel la carte est associée
        self.action = action  # L'action à effectuer (ajouter ou retirer)
        self.menu_gestion = menu_gestion  # Référence à la fenêtre de gestion des utilisateurs
        self.master.title(f"{action.capitalize()} Carte de Crédit")  # Titre de la fenêtre

        # Champ pour le numéro de carte de crédit
        self.label_numero_carte = tk.Label(master, text="Numéro de carte (8 chiffres)")
        self.label_numero_carte.grid(row=0, column=0)
        self.entry_numero_carte = tk.Entry(master)
        self.entry_numero_carte.grid(row=0, column=1)

        # Si l'action est d'ajouter une carte, afficher les champs supplémentaires
        if action == "ajouter":
            self.label_date_expire = tk.Label(master, text="Date d'expiration (MM/AA)")
            self.label_date_expire.grid(row=1, column=0)
            self.entry_date_expire = tk.Entry(master)
            self.entry_date_expire.grid(row=1, column=1)

            self.label_code_carte = tk.Label(master, text="Code (3 chiffres)")
            self.label_code_carte.grid(row=2, column=0)
            self.entry_code_carte = tk.Entry(master)
            self.entry_code_carte.grid(row=2, column=1)

        # Bouton pour exécuter l'action (ajouter ou retirer)
        self.button_action = tk.Button(master, text=f"{action.capitalize()} Carte", command=self.gerer_carte)
        self.button_action.grid(row=3, column=0)

        # Bouton pour fermer la fenêtre
        self.button_fermer = tk.Button(master, text="Fermer", command=self.master.destroy)
        self.button_fermer.grid(row=3, column=1)

    def gerer_carte(self):
        # Récupère le numéro de carte saisi par l'utilisateur
        numero_carte = self.entry_numero_carte.get()

        # Validation du champ numéro de carte
        if not numero_carte:
            messagebox.showerror("Erreur", "Le champ Numéro de carte doit être rempli.")
            return

        if not numero_carte.isdigit() or len(numero_carte) != 8:
            messagebox.showerror("Erreur", "Le numéro de carte doit être un nombre de 8 chiffres.")
            return

        # Si l'action est d'ajouter une carte
        if self.action == "ajouter":
            # Récupère la date d'expiration et le code de sécurité
            date_expire = self.entry_date_expire.get()
            code_carte = self.entry_code_carte.get()

            # Validation des champs date d'expiration et code de sécurité
            if not date_expire or not code_carte:
                messagebox.showerror("Erreur", "Tous les champs doivent être remplis.")
                return

            if not self.valider_date_expire(date_expire):
                messagebox.showerror("Erreur", "La date d'expiration doit être au format MM/AA.")
                return

            if not code_carte.isdigit() or len(code_carte) != 3:
                messagebox.showerror("Erreur", "Le code de la carte doit être un nombre de 3 chiffres.")
                return

            # Crée une nouvelle carte de crédit et l'ajoute au client
            carte = CarteCredit(numero_carte, date_expire, code_carte)
            self.client.cartes_credit.append(carte)
            messagebox.showinfo("Succès", "Carte de crédit ajoutée avec succès.")

        # Si l'action est de retirer une carte
        elif self.action == "retirer":
            # Cherche la carte dans la liste des cartes du client
            for c in self.client.cartes_credit:
                if c.numero == numero_carte:
                    # Supprime la carte si trouvée
                    self.client.cartes_credit.remove(c)
                    messagebox.showinfo("Succès", "Carte de crédit retirée avec succès.")
                    break
            else:
                # Affiche un message d'erreur si la carte n'est pas trouvée
                messagebox.showerror("Erreur", "Carte de crédit non trouvée.")

        # Met à jour la vue dans la fenêtre de gestion des utilisateurs
        self.menu_gestion.update_tree()
        # Ferme la fenêtre actuelle
        self.master.destroy()

    def valider_date_expire(self, date_expire):
        # Valide que la date d'expiration est au format MM/AA
        try:
            datetime.strptime(date_expire, '%m/%y')
            return True
        except ValueError:
            return False


if __name__ == "__main__":
    root = tk.Tk()
    app = MenuCartes(root, None)
    root.mainloop()

