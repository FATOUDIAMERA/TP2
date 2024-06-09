 def Ajouter_contact():
     Nom=input("Entrez le nom du contact \n")
     Prenom=input("Entrez le prenom \n")
     Tel=input("Entrez le tel ")
 MonFic=open("Contact.txt","a",encoding="utf8")
 MonFic.write(Nom + "\n")
 MonFic.write(Prenom + "\n")
 MonFic.write(Tel + "\n")
 MonFic.close
def Lister():
    MonFic=open("contact.txt","r",encoding="utf8")
    Uneligne=MonFic.readline()
    while Uneligne!="":
        print(Uneligne)
        Uneligne=MonFic.readline()
def Modifier_contact():
    print("Que voulez vous modifier\n") 
    print("Tapez 1 pour le Nom")
    print("Taper 2 pour le Prenom")
    print("Tapez 3 pour le Tel")
    choix=int(input("Faites votre choix"))
    if choix==1:
        annom=input("Quelle est le nom à Modifier")
        nvnom=input("Quelle est le nouveau nom")
        MonFic=open("contact.txt","r",encoding="utf8")
        tempon=open("temp.txt","w",encoding="utf8")
        LigNom=MonFic.readline()
        LigPrenom=MonFic.readline()
        LigTel=MonFic.readline()
        while LigNom!="" or LigPrenom!="" or LigTel!=""
            if choix==1:
                annom=input("Quelle est le Nom à Modifier ")
                nvnom=input("Quelle est le nouveau Nom ")
                MonFic=open("contact.txt","r",encoding="utf8")
                tempon=open("temp.txt","w",encoding="utf8")
                LigNom=MonFic.readline()
                LigPrenom=MonFic.readline()
                LigTel=MonFic.readline()
                while LigNom!="" or LigPrenom!="" or LigTel!="":
                    if LigNom==annom:
                        tempon.write(nvnom+ "\n")
                        tempon.write(LigPrenom+ "\n")
                        tempon.write(LigTel+ "\n")
                    else:
                        tempon.write(nvnom+ "\n")
                        tempon.write(LigPrenom+ "\n")
                        tempon.write(LigTel+ "\n")
                   
                    LigNom=MonFic.readline()
                    LigPrenom=MonFic.readline()
                    LigTel=MonFic.readline()
        MonFic.close()
        tempon.close()
        remove("contact.txt")
        renames("temp.txt," "contact.txt")
def supprimer_contact():
         nom_contact=input("donner le nom du contact à supprimer\n")
         MonFic=open("contact.txt","r",encoding="utf8")
         tempon=open("temp.txt","w",encoding="utf8")
         LigNom=MonFic.readline()
         LigPrenom=MonFic.readline()
         LigTel=MonFic.readline()
            while LigNom!="" or LigPrenom!="" or LigTel!="":
                 print(LigNom)
                 print(nom_contact)
                    if LigNom==annom:
                        tempon.write(nvnom+ "\n")
                        tempon.write(LigPrenom+ "\n")
                        tempon.write(LigTel+ "\n")
 LigNom=MonFic.readline()
                    LigPrenom=MonFic.readline()
                    LigTel=MonFic.readline()
        MonFic.close()
        tempon.close()
        remove("contact.txt")
        renames("temp.txt," "contact.txt")






