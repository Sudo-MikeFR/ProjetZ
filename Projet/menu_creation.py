import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from Classes import clients, Client, CarteCredit
from Menu_Quitter import menuquitter

### disposition de la fenetre de creation de clients
class MenuCreation:
    def __init__(self, master, menu_gestion):
        self.master = master
        self.menu_gestion = menu_gestion
        self.master.title("Création de Client")

        # Champs de saisie pour le client avec entry pour capturer l'information
        self.label_nom = tk.Label(master, text="Nom")
        self.label_nom.grid(row=0, column=0)
        self.entry_nom = tk.Entry(master)
        self.entry_nom.grid(row=0, column=1)

        self.label_prenom = tk.Label(master, text="Prénom")
        self.label_prenom.grid(row=1, column=0)
        self.entry_prenom = tk.Entry(master)
        self.entry_prenom.grid(row=1, column=1)

        self.label_sexe = tk.Label(master, text="Sexe")
        self.label_sexe.grid(row=2, column=0)
        self.entry_sexe = tk.Entry(master)
        self.entry_sexe.grid(row=2, column=1)

        self.label_date_inscription = tk.Label(master, text="Date d'inscription (YYYY-MM-DD)")
        self.label_date_inscription.grid(row=3, column=0)
        self.entry_date_inscription = tk.Entry(master)
        self.entry_date_inscription.grid(row=3, column=1)

        self.label_courriel = tk.Label(master, text="Courriel")
        self.label_courriel.grid(row=4, column=0)
        self.entry_courriel = tk.Entry(master)
        self.entry_courriel.grid(row=4, column=1)

        self.label_mot_de_passe = tk.Label(master, text="Mot de passe")
        self.label_mot_de_passe.grid(row=5, column=0)
        self.entry_mot_de_passe = tk.Entry(master, show="*")
        self.entry_mot_de_passe.grid(row=5, column=1)

        self.label_cartes = tk.Label(master, text="Cartes de Crédit")
        self.label_cartes.grid(row=6, columnspan=2)

        # Champs pour la carte de crédit
        self.label_numero_carte = tk.Label(master, text="Numéro de carte (8 chiffres)")
        self.label_numero_carte.grid(row=7, column=0)
        self.entry_numero_carte = tk.Entry(master)
        self.entry_numero_carte.grid(row=7, column=1)
        ##champt date d'expiration
        self.label_date_expire = tk.Label(master, text="Date d'expiration (MM/AA)")
        self.label_date_expire.grid(row=8, column=0)
        self.entry_date_expire = tk.Entry(master)
        self.entry_date_expire.grid(row=8, column=1)
        ## champ code 3 chiffres
        self.label_code_carte = tk.Label(master, text="Code (3 chiffres)")
        self.label_code_carte.grid(row=9, column=0)
        self.entry_code_carte = tk.Entry(master)
        self.entry_code_carte.grid(row=9, column=1)

        # Boutons
        self.button_ajouter = tk.Button(master, text="Ajouter", command=self.ajouter)
        self.button_ajouter.grid(row=10, column=0)

        self.button_fermer = tk.Button(master, text="Fermer", command=self.master.destroy)
        self.button_fermer.grid(row=10, column=1)
## pour le bouton ajouter plus haut
    def ajouter(self):
        #### ajout des entrées et les encapsuler
        nom = self.entry_nom.get()
        prenom = self.entry_prenom.get()
        sexe = self.entry_sexe.get()
        date_inscription = self.entry_date_inscription.get()
        courriel = self.entry_courriel.get()
        mot_de_passe = self.entry_mot_de_passe.get()
        numero_carte = self.entry_numero_carte.get()
        date_expire = self.entry_date_expire.get()
        code_carte = self.entry_code_carte.get()
        ### si aucune entrée n'à été mise
        # Validation des champs
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
        if not self.courriel_unique(courriel):
            messagebox.showerror("Erreur", "Le courriel doit être unique.")
            return
            ## si les numéros de cartes n'est pas un numéro et n'égale pas à 8
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

        # Ajouter le nouveau client
        nouveau_client = Client(nom, prenom, sexe, date_inscription, courriel, mot_de_passe)
        nouveau_client.cartes_credit.append(CarteCredit(numero_carte, date_expire, code_carte))
        clients.append(nouveau_client)
        self.menu_gestion.update_tree()  # Mettre à jour la Treeview
        messagebox.showinfo("Succès", "Client ajouté avec succès.")
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

    #### vérifie si le courriel n'existe pas dans les clients
    def courriel_unique(self, courriel):
        # Parcourt tous les clients de la liste des clients
        for client in clients:
            # Vérifie si le courriel du client actuel correspond au courriel fourni
            if client.courriel == courriel:
                # Si une correspondance est trouvée, renvoie False indiquant que le courriel n'est pas unique
                return False
            # Si aucune correspondance n'est trouvée, renvoie True indiquant que le courriel est unique
        return True



if __name__ == "__main__":
    root = tk.Tk()
    app = MenuCreation(root, None)
    root.mainloop()
