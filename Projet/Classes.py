from typing import List

### Toutes les classes et les exemples de clients, acteurs, films, employe sont aussi ici --->


# Classe de base représentant une personne
class Personne:
    def __init__(self, nom: str, prenom: str, sexe: str):
        self.nom = nom
        self.prenom = prenom
        self.sexe = sexe

# Classe Client héritant de Personne
class Client(Personne):
    def __init__(self, nom: str, prenom: str, sexe: str, date_inscription: str, courriel: str, password: str):
        super().__init__(nom, prenom, sexe)
        self.date_inscription = date_inscription  # Date d'inscription
        self.courriel = courriel  # Courriel unique
        self.password = password  # Mot de passe
        self.cartes_credit: List[CarteCredit] = []  # Liste pour les cartes de crédit

# Classe Acteur héritant de Personne
class Acteur(Personne):
    def __init__(self, nom: str, prenom: str, sexe: str, date_debut_emploi: str, date_fin_emploi: str, nom_personnage: str, salaire: str):
        super().__init__(nom, prenom, sexe)
        self.date_debut_emploi = date_debut_emploi  # Date de début d'emploi
        self.date_fin_emploi = date_fin_emploi  # Date de fin d'emploi
        self.nom_personnage = nom_personnage  # Nom du personnage joué
        self.salaire = salaire  # Salaire de l'acteur

# Classe Employe héritant de Personne
class Employe(Personne):
    def __init__(self, nom: str, prenom: str, sexe: str, date_debut_emploi: str, username: str, password: str, type_acces: str):
        super().__init__(nom, prenom, sexe)
        self.date_debut_emploi = date_debut_emploi  # Date de début d'emploi
        self.username = username  # Nom d'utilisateur
        self.password = password  # Mot de passe
        self.type_acces = type_acces  # Type d'accès (admin ou lecture)

# Classe représentant une carte de crédit
class CarteCredit:
    def __init__(self, numero: str, date_expire: str, secret: str):
        self.numero = numero  # Numéro de la carte
        self.date_expire = date_expire  # Date d'expiration
        self.secret = secret  # Code secret (3 chiffres)

# Classe représentant un film
class Film:
    def __init__(self, nom_film: str, duree_film: str, description_film: str):
        self.nom_film = nom_film  # Nom du film
        self.duree_film = duree_film  # Durée du film
        self.description_film = description_film  # Description du film
        self.categories: List[Categorie] = []  # Liste des catégories
        self.acteur: List[Acteur] = [] # Liste des acteurs

# Classe représentant une catégorie de film
class Categorie:
    def __init__(self, nom_categorie: str, description_categorie: str):
        self.nom_categorie = nom_categorie  # Nom de la catégorie
        self.description_categorie = description_categorie  # Description de la catégorie

# Exemple d'employés
exemple_employe = [
    Employe(nom="test", prenom="test", sexe="M", date_debut_emploi="2024-01-06", username="admin", password="admin", type_acces="admin"),
    Employe(nom="test2", prenom="test2", sexe="M", date_debut_emploi="2024-01-06", username="test", password="test", type_acces="lecture")
]

# Exemple de clients
clients = [
    Client(nom="Doe", prenom="John", sexe="M", date_inscription="2024-01-01", courriel="john.doe@example.com", password="password123"),
    Client(nom="Smith", prenom="Jane", sexe="F", date_inscription="2024-02-01", courriel="jane.smith@example.com", password="password456")
]

# Exemple de films
films = [
    Film(nom_film="Inception", duree_film="2h28m", description_film="A mind-bending thriller"),
    Film(nom_film="The Matrix", duree_film="2h16m", description_film="A science fiction classic"),
    Film(nom_film="test", duree_film="2h33m", description_film="test"),
    Film(nom_film="test4", duree_film="2h56m", description_film="Bon film")
]

# Ajout de catégories à ces films
films[0].categories.append(Categorie(nom_categorie="Thriller", description_categorie="A thrilling movie"))
films[1].categories.append(Categorie(nom_categorie="Science Fiction", description_categorie="A sci-fi movie"))
films[2].categories.append(Categorie(nom_categorie="test2", description_categorie="qweq"))
films[3].categories.append(Categorie(nom_categorie="test5", description_categorie="sasd"))

## Ajout d'exemple carte de crédit
clients[1].cartes_credit.append((CarteCredit("12345678","11/11","123")))

#ajout d'acteur dans film ainsi que des exemples :
films[1].acteur.append((Acteur(nom="DiCaprio", prenom="Leonardo", sexe="M", date_debut_emploi="2010-07-16", date_fin_emploi="", nom_personnage="Dom Cobb", salaire="20000000")))
films[2].acteur.append((Acteur(nom="Reeves", prenom="Keanu", sexe="M", date_debut_emploi="1999-03-31", date_fin_emploi="", nom_personnage="Neo", salaire="15000000")))
films[3].acteur.append((Acteur(nom="DiCaprio", prenom="Leonardo", sexe="M", date_debut_emploi="2010-07-16", date_fin_emploi="", nom_personnage="Dom Cobb", salaire="20000000")))
films[0].acteur.append((Acteur(nom="Reeves", prenom="Keanu", sexe="M", date_debut_emploi="1999-03-31", date_fin_emploi="", nom_personnage="Neo", salaire="15000000")))