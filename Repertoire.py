while True :
    print("***Repertoire Telephonique*** \n")
    print("1.Ajouter un contact \n")
    print("2.Modifier un contact \n")
    print("3.Supprimer un contact")
    print("4.Lister les contacts \n")
    print("5.Rechercher un contact par le nom")
    print("6.Quitter")
    choix=int(input("FAites votre choix "))
    if choix==6:
        break
    if choix==1 :
        Ajouter_contact()
        if choix==4 :
            Lister()
        