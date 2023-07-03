import random
listeDocteur = []
listepatient =[]

##########################################################################
# code simulant une gestion d'hopital                                    #
# by lmr_lumiere                                                         #              
# proposer par espacesis                                                 #
##########################################################################

#############fonction pour l'erengistrement des docteurs##################
def enregisterDocteur():
    docteur = []
    nomDocteur = input("Entrez le nom du docteur: ")
    docteur.append(nomDocteur)
    postnomDocteur = input("Entrez le post-nom du docteur: ")
    docteur.append(postnomDocteur)
    prenomDocteur = input("Entrez le prenom du docteur: ")
    docteur.append(prenomDocteur)
    specialisationDocteur = input("Entrez la specialisation du docteur: ")
    docteur.append(specialisationDocteur)
    numerodocteur = input("Entrez le numero du docteur: ")
    docteur.append(numerodocteur)
    matricule = input("Entrez le matricule du docteur: ")
    docteur.append(matricule)
    genre = input("Entrez la genre du docteur (M/F): ")
    docteur.append(genre)

    listeDocteur.append(docteur)
    #print(docteur)

#enregisterDocteur()
############fonction pour l'enregistrement des patients####################
def enregistrerpatient():
    patient = []
    id_count=1
    nompatient = input("Entrez le nom du patient: ")
    patient.append(nompatient)
    prenonpatient = input("Entrez le prenom du patient: ")
    patient.append(prenonpatient)
    postnompatient = input("Entrez le postnom du patient: ")
    patient.append(postnompatient)
    poids = int(input("Entrez le poids du patient(kg): "))
    patient.append(poids)
    taille = float(input("Entrez la taille du patient (métre): "))
    patient.append(taille)
    genre = input("Entrez le genre du patient: ")
    patient.append(genre)
    age = input("Entrez l'age du patient (01-01-2023): ")
    patient.append(age)
    #patient.append(imc)
    numeropatient = "".join(random.choices("1234567890abcdefghijklmnopqrstuvwxyz", k=4) )
    ordre="".join(random.choices("1234567890", k=3))
    
    id_patient= age[8:10] +nompatient[0] + postnompatient[0] + ordre
    patient.append(id_patient)
    patient.append(numeropatient)

    listepatient.append(patient)
################afficher tous les patients#################################
def affichertouspatient():
    for i in listepatient:
        if i :
            print(i)
        elif i == "":
            print("la liste est vide ")
    

################afficher tous les docteurs################################
def affichertousdocteur():
    for i in listeDocteur:
        if i:
            print(i)
        elif i == "":
            print("la liste est vide ")

################chercher un patient avec ses identite#####################
def chercherpatientnom(nom,prenom,postnom):
    chercher_patient = []
    chercher_patient.append(nom)
    chercher_patient.append(prenom)
    chercher_patient.append(postnom)
    # nontrouver = "N'est pas trouver dans la liste"
    afficher = []
    
    for i in range(len(listepatient)):
        for j in listepatient[i]:
            if chercher_patient[0] == listepatient [i][0] and  chercher_patient[1] ==listepatient [i][1] and  chercher_patient[2] ==listepatient [i][2]:
                afficher = f'\nPrénom : {listepatient[i][0]}\nNom: {listepatient[i][1]}\n Postnom: {listepatient[i][2]}\nPoids : {listepatient[i][3]}\nTaille : {listepatient[i][4]}\nGenre : {listepatient[i][5]}\nAge : {listepatient[i][6]}\nNumero de telephone : {listepatient[i][7]}\nNuméro du dossier :{listepatient[i][8]}'
                return afficher
                break
            else:
                return ("aucun resultat ...")
            

###############rechercher docteur avec ses identiter #####################
def chercherdocteurnom(nom,postnom,prenom):
    if len(listeDocteur) > 0:
        for i in range(len(listeDocteur)):
            return f'\nNom : {listeDocteur[i][0]}\nPost-nom: {listeDocteur[i][1]}\nPrenon: {listeDocteur[i][2]}\nSpécialité : {listeDocteur[i][3]}\nNuméro de téléphone : {listeDocteur[i][4]}\nMatricule : {listeDocteur[i][5]}\nGenre : {listeDocteur[i][6]}\n'
    else :
        return ("La liste est encore vide !")

###############ajouter plainte#####################################
listeplainte=[]
def ajoutplainte():
    plainte=[]
    pl=input("entrez votrre plainte ")
    plainte.append(pl)
    listeplainte.append(plainte)

#################afficher les plaintes ###########################
def afficherplainte():
    for i in listeplainte:
        if i :
            print(i)
        elif i =='':
            print("la liste des plaintes est vide ")

##################calcule de l'imc ###############################
def calcule_imc(poids, taille):
    indice = poids/ taille**2
    if indice < 18.5:
        imc="Insuffisance pondérale (maigreur)"
    elif indice >= 18.5 and indice< 25:
        imc = "Corpulence normale"
    elif indice >= 25 and indice< 30:
        imc = "Surpoids"
    elif indice >= 30 and indice < 35:
        imc = "Obésité modérée"
    elif indice >= 35 and indice < 40:
        imc = "Obésité sévère"
    elif indice > 40:
        imc = "Obésité morbide ou massive"
    return f"votre indice est de {indice} et vous etes {imc}"

#############ajouter l'horaire d'un medecin ################
def ajouter_horaire(prenom, nom, postnom):
    identifiants = []
    horaire = []
    identifiants.append(prenom)
    identifiants.append(nom)
    identifiants.append(postnom)
    nontrouver = "N'est pas trouver dans la liste"
    for i in range(len(listeDocteur)):
        for j in listeDocteur:
            if  identifiants[0] == listeDocteur[i][0] and identifiants[1] == listeDocteur[i][1] and identifiants[2] == listeDocteur[i][2]:
                jour1 = input("Entrez son horaire du lundi: ")
                jour2 = input("Entrez son horaire du mardi: ")
                jour3 = input("Entrez son horaire du mercredi: ")
                jour4 = input("Entrez son horaire du jeudi: ")
                jour5 = input("Entrez son horaire du vendredi: ")
                jour6 = input("Entrez son horaire du samedi: ")
                jour7 = input("Entrez son horaire du dimanche: ")
                horaire.append(jour1)
                horaire.append(jour2)
                horaire.append(jour3)
                horaire.append(jour4)
                horaire.append(jour5)
                horaire.append(jour6)
                horaire.append(jour7)
                #horaire(jour1, jour2, jour3, jour4, jour5, jour6, jour7)
                listeDocteur[i].append(horaire)
                break
            else:
                return nontrouver

#############afficher l'horaire d'un mediecin#################

def afficher_horaire(prenom, nom, postnom):
    afficher = []
    chercher_docteur = []
    chercher_docteur.append(prenom)
    chercher_docteur.append(nom)
    chercher_docteur.append(postnom)
    nontrouver = "N'est pas trouver dans la liste"
    for i in range(len(listeDocteur)):
        if len(listeDocteur[i]) >= 8:
            for j in listeDocteur:
                if chercher_docteur[0] == listeDocteur[i][0] and chercher_docteur[1] == listeDocteur[i][1] and chercher_docteur[2] == listeDocteur[i][2]:
                    afficher = f'Prénom : {listeDocteur[i][0]}\nNom: {listeDocteur[i][1]}\nPostnom : {listeDocteur[i][2]}\nVoici son horaire :\n     Lundi :{listeDocteur[i][7][0]}\n       Mardi :{listeDocteur[i][7][1]}\n       Mercredi :{listeDocteur[i][7][2]}\n        Jeudi :{listeDocteur[i][7][3]}\n      Vendredi :{listeDocteur[i][7][4]}\n       Samedi{listeDocteur[i][7][5]}\n       Dimanche :{listeDocteur[i][7][6]}'
                    return afficher
                    break
                else:

                    return nontrouver



###################fonction principale #######################
def fonctionprincipale():
    print("="*57)
    print("||  bienvenue dans notre systeme de gestion d'hopitale  ||")
    print("||"," "*52,"||")
    print("="*57 ,"\n")
    print("="*63)
    print(" veillez choisir le numero de l'option que vous voulez utiliser\n"+"="*63)
    print("\
           1.Enregistrer un docteur \n \
          2.Enregistrer un patient \n \
          3.Afficher tous les Docteurs \n \
          4.Afficher tous les Patients \n \
          5.ajouter une plainte \n \
          6.afficher les plaintes \n \
          7.Rechercher un medecin \n \
          8.Rechercher un patient \n \
          9.ajouter l'horaire d'un medicin \n \
          10.afficher l'horaire de medecin \n \
          0. to exit")
    choix=input(">>> ")
    if choix == "0":
        exit()
    elif choix == "1":
        print("="*60)
        print(" bienvenue a l'enregistrements des docteurs ")
        print("="*60)
        return enregisterDocteur()
    elif choix == "2":
        print("="*60)
        print(" bienvenue a l'enegistrement des patients ")
        print("="*60)
        return enregistrerpatient()
    elif choix == "3":
        print("="*60)
        print(" bienvenue a l'affichage des medecins ")
        print("="*60)
        return affichertousdocteur()
    elif choix == "4":
        print("="*60)
        print(" bienvenue a l'affichage des patients ")
        print("="*60)
        return affichertouspatient()
    elif choix == "5":
        print("="*60)
        print(" bienvenue a l'ajouts des plaintes  ")
        print("="*60)
        return ajoutplainte()
    elif choix == "6":
        print("="*60)
        print(" bienvenue a l'affichage des plaintes des patient  ")
        print("="*60)
        return afficherplainte()
    elif choix == "7":
        print("="*60)
        print(" bienvenue a la recherche d'un docteur  ")
        print("="*60)
        prenom = input("Entrez le prenom du docteur pour leque vous voulez rechercher: ")
        nom = input("Entrez le nom du docteur pour leque vous voulez rechercher: ")
        postnom = input("Entrez le postnom du docteur pour leque vous voulez rechercher: ")
        print(chercherdocteurnom(nom,prenom,postnom))
    elif choix =="8":
        print("="*60)
        print(" bienvenue a la recherche de patient ")
        print("="*60)
        prenom = input("Entrez le prenom du patient pour leque vous voulez rechercher: ")
        nom = input("Entrez le nom du patient pour leque vous voulez rechercher: ")
        postnom = input("Entrez le postnom du patient pour leque vous voulez recherche: ")
        print(chercherpatientnom(nom,prenom,postnom))
    elif choix == "9":
        print("="*60)
        print(" bienvenue a l'ajout de l'horaire des medecin ")
        print("="*60)
        prenom=input("entrer le prenom du docteur que vous vollez ajouter a l'horaire ")
        nom=input("entrer le nom du docteur que vous vollez ajouter a l'horaire ")
        postnom=input("entrer le post-nom du docteur que vous vollez ajouter a l'horaire ")
        print(ajouter_horaire(nom,postnom,prenom))
    elif choix == "10":
        print("="*60)
        print(" bienvenue a l'affichage de l'horaire ")
        print("="*60)
        prenom=input("entrer le prenom du docteur que vous vollez voir l'horaire ")
        nom=input("entrer le nom du docteur que vous vollez voir l'horaire ")
        postnom=input("entrer le post-nom du docteur que vous vollez voir l'horaire ")
        print(afficher_horaire(nom,postnom,prenom))
while True:

    fonctionprincipale()
