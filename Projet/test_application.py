import unittest
from datetime import datetime
from Classes import Client, CarteCredit, clients

##faire les tests utilitaires :
class TestClientMethods(unittest.TestCase):

    def setUp(self):
        # Cette méthode sera appelée avant chaque test
        self.client = Client(nom="Doe", prenom="John", sexe="M", date_inscription="2024-01-01",
                             courriel="john.doe@example.com", password="password")
        self.carte = CarteCredit(numero="12345678", date_expire="12/24", secret="123")
        self.client.cartes_credit.append(self.carte)
        clients.append(self.client)

    def tearDown(self):
        # Cette méthode sera appelée après chaque test
        clients.clear()

    def test_creation_client(self):
        # Test de la création d'un client
        self.assertEqual(self.client.nom, "Doe")
        self.assertEqual(self.client.prenom, "John")
        self.assertEqual(self.client.sexe, "M")
        self.assertEqual(self.client.date_inscription, "2024-01-01")
        self.assertEqual(self.client.courriel, "john.doe@example.com")
        self.assertEqual(self.client.password, "password")
        self.assertEqual(len(self.client.cartes_credit), 1)

    def test_ajouter_carte_credit(self):
        # Test d'ajout d'une carte de crédit
        nouvelle_carte = CarteCredit(numero="87654321", date_expire="11/23", secret="321")
        self.client.cartes_credit.append(nouvelle_carte)
        self.assertEqual(len(self.client.cartes_credit), 2)
        self.assertEqual(self.client.cartes_credit[1].numero, "87654321")

    def test_modifier_client(self):
        # Test de la modification d'un client
        self.client.nom = "Smith"
        self.client.prenom = "Jane"
        self.client.sexe = "F"
        self.client.date_inscription = "2024-02-01"
        self.client.courriel = "jane.smith@example.com"
        self.client.password = "newpassword"
        self.assertEqual(self.client.nom, "Smith")
        self.assertEqual(self.client.prenom, "Jane")
        self.assertEqual(self.client.sexe, "F")
        self.assertEqual(self.client.date_inscription, "2024-02-01")
        self.assertEqual(self.client.courriel, "jane.smith@example.com")
        self.assertEqual(self.client.password, "newpassword")

    def test_supprimer_client(self):
        # Test de la suppression d'un client
        clients.remove(self.client)
        self.assertNotIn(self.client, clients)

    def test_valider_date_inscription(self):
        # Test de validation de la date d'inscription
        try:
            datetime.strptime(self.client.date_inscription, '%Y-%m-%d')
            valid = True
        except ValueError:
            valid = False
        self.assertTrue(valid)

    def test_valider_date_expire(self):
        # Test de validation de la date d'expiration de la carte de crédit
        try:
            datetime.strptime(self.carte.date_expire, '%m/%y')
            valid = True
        except ValueError:
            valid = False
        self.assertTrue(valid)


if __name__ == '__main__':
    unittest.main()
