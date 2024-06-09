# nom programme : test_tkinter0.py
from tkinter import *

# creation d'un objet "fenêtre"
fenetre=Tk()  # nouvelle instance de Tk
fenetre.title("connexion")
fenetre.geometry("600x400")

# pour saisir identifiant
label1=Label(fenetre,text="Login")
champ1=Entry(fenetre,width=30)
label1.pack()
champ1.pack()

# pour saisir mot de passe
label2=Label2(fenetre,text="Password")
champ2=Entry(fenetre,width=30)
label2.pack()
champ2.pack()

# Bouton de comande
bouton1 = Button(fenetre, text = "connexion")
bouton1.pack()

# Bouton de comande
bouton2 = Button(fenetre, text = "annuler")
bouton2.pack()

# Affichage de la fenêtre
fenetre.mainloop()



