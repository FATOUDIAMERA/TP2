nomFic=input("donner le nom du fichier à creer")
MonFichier=open(Nomfic,"w",encoding="utf-8")
Nomcontact=input("donner un nom de contact")
Tel=input("donner un numéro de telephone")
MonFichier.write(nomcontact)
MonFichier.write(Tel)

Monfichier.close