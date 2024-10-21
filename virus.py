import tkinter as tk
import random

# Liste de titres de fenêtres
window_titles = [
    "Attention !",
    "Alerte Système !",
    "Fenêtre Intrusive !",
    "Message Importante !",
    "Avertissement !",
    "Erreur Inconnue !",
    "Notification Étrange !"
]

# Liste de messages aléatoires
random_texts = [
    "Votre attention est requise !",
    "Ne fermez pas cette fenêtre.",
    "Votre système fonctionne lentement.",
    "Une mise à jour est disponible !",
    "Cliquez ici pour plus d'informations.",
    "Une erreur s'est produite, veuillez redémarrer.",
    "Des publicités sont en attente d'affichage.",
    "Vous avez gagné un prix ! Réclamez-le maintenant !"
]

def create_window():
    window = tk.Tk()
    
    # Choisir un titre et un texte aléatoire
    title = random.choice(window_titles)
    text = random.choice(random_texts)
    
    window.title(title)
    
    label = tk.Label(window, text=text)
    label.pack(padx=70, pady=40)
    window.geometry("700x500")  # Définir la taille de la fenêtre
    window.mainloop()

# Créer trois fenêtres avec des textes et titres aléatoires
for i in range(3):
    create_window()
