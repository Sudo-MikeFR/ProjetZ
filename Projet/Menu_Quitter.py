import tkinter as tk

## menu pour quand je fait le X de l'application, si je ne mets pas ça, je recois un message d'erreur..
class menuquitter:
    def __init__(self, master, is_main_window=False):
        # Initialisation de la fenêtre principale
        self.master = master
        # Indique si cette fenêtre est la fenêtre principale de l'application
        self.is_main_window = is_main_window
        # Associe la méthode on_closing à l'événement de fermeture de la fenêtre
        self.master.protocol("WM_DELETE_WINDOW", self.on_closing)

    def on_closing(self):
        # Détruit la fenêtre actuelle
        self.master.destroy()
        # Si cette fenêtre est la fenêtre principale, arrête la boucle principale de Tkinter
        if self.is_main_window:
            self.master.quit()
