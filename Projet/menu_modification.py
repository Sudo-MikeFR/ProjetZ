import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from Classes import clients, Client, CarteCredit
from Menu_Quitter import menuquitter


## disposition de la fenetre
class MenuModification:
    ## il faut avoir avoir le client ainsi que le choix de la personne pour marqué les bonnes informations dans les champs
    ##prends les informations dans menu_gestion
    def __init__(self, master, menu_gestion, client):
        self.master = master
        self.menu_gestion = menu_gestion
        self.client = client  # Informations du client à modifier
        self.master.title("Modification du Client")

        # Champs de saisie pour le client
        self.label_nom = tk.Label(master, text="Nom")
        self.label_nom.grid(row=0, column=0)
        self.entry_nom = tk.Entry(master)
        self.entry_nom.grid(row=0, column=1)
        self.entry_nom.insert(0, client.nom)  # Préremplir avec le nom du client

        self.label_prenom = tk.Label(master, text="Prénom")
        self.label_prenom.grid(row=1, column=0)
        self.entry_prenom = tk.Entry(master)
        self.entry_prenom.grid(row=1, column=1)
        self.entry_prenom.insert(0, client.prenom)  # Préremplir avec le prénom du client

        self.label_sexe = tk.Label(master, text="Sexe")
        self.label_sexe.grid(row=2, column=0)
        self.entry_sexe = tk.Entry(master)
        self.entry_sexe.grid(row=2, column=1)
        self.entry_sexe.insert(0, client.sexe)  # Préremplir avec le sexe du client

        self.label_date_inscription = tk.Label(master, text="Date d'inscription (YYYY-MM-DD)")
        self.label_date_inscription.grid(row=3, column=0)
        self.entry_date_inscription = tk.Entry(master)
        self.entry_date_inscription.grid(row=3, column=1)
        self.entry_date_inscription.insert(0, client.date_inscription)  # Préremplir avec la date d'inscription du client

        self.label_courriel = tk.Label(master, text="Courriel")
        self.label_courriel.grid(row=4, column=0)
        self.entry_courriel = tk.Entry(master)
        self.entry_courriel.grid(row=4, column=1)
        self.entry_courriel.insert(0, client.courriel)  # Préremplir avec le courriel du client

        self.label_mot_de_passe = tk.Label(master, text="Mot de passe")
        self.label_mot_de_passe.grid(row=5, column=0)
        self.entry_mot_de_passe = tk.Entry(master, show="*")
        self.entry_mot_de_passe.grid(row=5, column=1)
        self.entry_mot_de_passe.insert(0, client.password)  # Préremplir avec le mot de passe du client

        self.label_cartes = tk.Label(master, text="Cartes de Crédit")
        self.label_cartes.grid(row=6, columnspan=2)

        # Champs pour la carte de crédit (afficher la première carte si elle existe)
        self.label_numero_carte = tk.Label(master, text="Numéro de carte (8 chiffres)")
        self.label_numero_carte.grid(row=7, column=0)
        self.entry_numero_carte = tk.Entry(master)
        self.entry_numero_carte.grid(row=7, column=1)
        if client.cartes_credit:
            self.entry_numero_carte.insert(0, client.cartes_credit[0].numero)

        self.label_date_expire = tk.Label(master, text="Date d'expiration (MM/AA)")
        self.label_date_expire.grid(row=8, column=0)
        self.entry_date_expire = tk.Entry(master)
        self.entry_date_expire.grid(row=8, column=1)
        if client.cartes_credit:
            self.entry_date_expire.insert(0, client.cartes_credit[0].date_expire)

        self.label_code_carte = tk.Label(master, text="Code (3 chiffres)")
        self.label_code_carte.grid(row=9, column=0)
        self.entry_code_carte = tk.Entry(master)
        self.entry_code_carte.grid(row=9, column=1)
        if client.cartes_credit:
            self.entry_code_carte.insert(0, client.cartes_credit[0].secret)

        # Boutons
        self.button_modifier = tk.Button(master, text="Modifier", command=self.modifier)
        self.button_modifier.grid(row=10, column=0)

        self.button_fermer = tk.Button(master, text="Fermer", command=self.master.destroy)
        self.button_fermer.grid(row=10, column=1)

        ##remplir les différentes sections
    def modifier(self):
        nom = self.entry_nom.get()
        prenom = self.entry_prenom.get()
        sexe = self.entry_sexe.get()
        date_inscription = self.entry_date_inscription.get()
        courriel = self.entry_courriel.get()
        mot_de_passe = self.entry_mot_de_passe.get()
        numero_carte = self.entry_numero_carte.get()
        date_expire = self.entry_date_expire.get()
        code_carte = self.entry_code_carte.get()

        # Validation des champs (même validation que la creation)
        if not nom or not prenom or not sexe or not date_inscription or not courriel or not mot_de_passe or not numero_carte or not date_expire or not code_carte:
            messagebox.showerror("Erreur", "Tous les champs doivent être remplis.")
            return
        ## si le sexe n'est pas : {"F", "M", "f", "m"}: , message d'erreur
        if sexe not in {"F", "M", "f", "m"}:
            messagebox.showerror("Erreur", "Le sexe doit être M ou F.")
            return
        ### si la date n'est pas dans le bon format , (def plus bas) , la date doit être dans le format YYYY-MM-DD
        if not self.valider_date_inscription(date_inscription):
            messagebox.showerror("Erreur", "La date d'inscription doit être au format YYYY-MM-DD.")
            return
        ###si le mot de passe est en bas de 8 caractères
        if len(mot_de_passe) < 8:
            messagebox.showerror("Erreur", "Le mot de passe doit contenir au moins 8 caractères.")
            return
        ### voit si le courriel est unique (def plus bas), s'il existe dans la liste de client, message d'erreur
        if not self.courriel_unique(courriel, self.client):
            messagebox.showerror("Erreur", "Le courriel doit être unique.")
            return

        if not numero_carte.isdigit() or len(numero_carte) != 8:
            messagebox.showerror("Erreur", "Le numéro de carte doit être un nombre de 8 chiffres.")
            return
        ### valide la date (def plus bas) attent le format mm/aa (utilise datetime)
        if not self.valider_date_expire(date_expire):
            messagebox.showerror("Erreur", "La date d'expiration doit être au format MM/AA.")
            return
        ###si les codes n'est pas des chiffres et est plus petit que 3
        if not code_carte.isdigit() or len(code_carte) != 3:
            messagebox.showerror("Erreur", "Le code de la carte doit être un nombre de 3 chiffres.")
            return

        # Mettre à jour les informations du client
        self.client.nom = nom
        self.client.prenom = prenom
        self.client.sexe = sexe
        self.client.date_inscription = date_inscription
        self.client.courriel = courriel
        self.client.password = mot_de_passe

        if self.client.cartes_credit:
            self.client.cartes_credit[0].numero = numero_carte
            self.client.cartes_credit[0].date_expire = date_expire
            self.client.cartes_credit[0].secret = code_carte
        else:
            self.client.cartes_credit.append(CarteCredit(numero_carte, date_expire, code_carte))

        # Mettre à jour la liste des clients dans menu_gestion
        # Boucle à travers tous les clients pour trouver le client actuel
        for i, client in enumerate(clients):
            # Vérifie si le courriel du client dans la liste correspond à celui du client modifié
            if client.courriel == self.client.courriel:
                # Si une correspondance est trouvée, met à jour ce client dans la liste avec les nouvelles informations
                clients[i] = self.client
                # Sort de la boucle une fois le client mis à jour
                break
            ## MAJ de la liste dans menu_gestion
        self.menu_gestion.tree.item(self.menu_gestion.tree.selection()[0], values=(nom, prenom, courriel))
        self.menu_gestion.update_tree()  # Mettre à jour la Treeview
        messagebox.showinfo("Succès", "Client modifié avec succès.")
        self.master.destroy()

        ### s'assurer que la date est dans le bon format '%Y-%m-%d utilise datetime
    def valider_date_inscription(self, date_inscription):
        try:
            datetime.strptime(date_inscription, '%Y-%m-%d')
            return True
        except ValueError:
            return False

    ### s'assurer que la date est dans le bon format '%m/%y' utilise datetime
    def valider_date_expire(self, date_expire):
        try:
            datetime.strptime(date_expire, '%m/%y')
            return True
        except ValueError:
            return False
### vérifie si le courriel est unique
    def courriel_unique(self, courriel, current_client):
        for client in clients:
            if client.courriel == courriel and client != current_client:
                return False
        return True

if __name__ == "__main__":
    root = tk.Tk()
    app = MenuModification(root, None)
    root.mainloop()
