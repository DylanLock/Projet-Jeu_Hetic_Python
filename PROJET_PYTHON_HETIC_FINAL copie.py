import random
import time

#saluer le joueur et écrire les informations :

print("Yo bienvenue dans le jeu")
time.sleep(1.5)
#saut de ligne
print("\n")
print("Ceci est un simulateur d'insulte, il demande de connaitre les bases de python notamment l'indexation de liste")


print("A LIRE ATTENTIVEMENT AVANT DE COMMENCER")

#saut de ligne
print("\n")

print("Pour choisir vos persos ou vos mots, utilisez des nombres")
print("0 est le premier element de la liste, -1 est le premier element de la liste partant de la fin ")
print("Vous n'aurez qu'a rentrer dans la console ci dessous des nombres")
print("Le jeu se joue a deux joueurs tour par tour sur le même clavier")

#saut de ligne
print("\n")

#Avez vous lu les consignes/ bouton de demarrage du jeu
print("Avez vous bien lu les règles?")
activation=input("J'ai fini de lire(Taper 1)")

if activation=="1":
    print("Bon jeu")
    print("\n")
    print("\n")


    #définir les classes des personnages
    #écrire les descriptions des personnages


    #fonctions pour chercher un truc au hasard :



    def randomizer(seq,n):
        result=random.sample(seq,n)

        return result




    #définir les classes des mots : adverbes, etc

    class Mots:
        def __init__(self, grammaire, force,orthographe):
            self.grammaire = grammaire
            self.force = force
            self.orthographe= orthographe



    FBI = Mots("mot commun", "Six9ine", "Le FBI")
    Album = Mots("mot commun", "Six9ine","L'Album")
    Pauvre = Mots("mot commun", "Six9ine","Pauvre")
    chicha = Mots("mot commun","JUL","chicha")
    balance = Mots("mot commun","Six9ine","une balance")
    caca = Mots("mot commun","none","le caca")

    recycler = Mots("verbe","JUL","recycler")
    avoir = Mots("verbe","none","avoir")
    être = Mots("verbe","none","es")
    tellement = Mots("adverbe","none","tellement")
    tout = Mots("adverbe","none","tout")
    avec = Mots("adverbe","none","avec")
    rien = Mots("adverbe","none","rien")
    sur = Mots("adverbe","none","sur")
    ton = Mots("possessif","none","ton")
    tes = Mots("possessif","none","tes")
    Tu = Mots("sujet","none","Tu")
    Petit =Mots("mot commun","Lil_Pump","petit")

    Yaourt =Mots("mot commun","Lil_Pump","yaourt")
    signe_astrologique =Mots("mot commun","Six9ine","signe astrologique")

    Joueur1 = Mots("none","none","Joueur1")
    Joueur2 = Mots("none","none","Joueur2")





    #mettre systeme de point

    # print(FBI.grammaire)

    Sujet=[
     Tu]

    #Pas beson de plus de pronom possessif
    pronom_possessif=[ton ,
     tes]




    liste_mot=[
    Album,
    Yaourt,
    Petit,
    Pauvre,
    # Revenu,
    # ignorant,
    # enfantin,
    # cigarette,
    balance ,
    FBI ,

    signe_astrologique ,

    caca ,
    chicha ,
    # ingénieur_son
    ]

    verbes=[
    recycler,
    # pue,
    # ressemble,
    # gagner,
    # perdre,
    # vendre,
    être,
    avoir]


    adverbe=[
    tellement,
    # heureusement,
    # malheuresement,
    tout,
    # tous,
    # après,
    sur,
    avec ,

    rien
    ]



    #appeler les différents mots
        #appeler les verbes
        #appeler les mots check






    print("\n")
    jouer = "y"
    while jouer == "y":

        #appeler la fonction et mettre les arguments :
        #rassembler verbes

        #la liste du round, vide au départ
        round_list=[]
        #utiliser la fonction randomizer
        A=randomizer(verbes,3)
        B=randomizer(adverbe,3)
        C=randomizer(liste_mot,3)
        D=randomizer(pronom_possessif,2)
        E=randomizer(Sujet,1)
        #rallonger la liste avec la liste de verbe
        round_list.extend(A)
        round_list.extend(B)
        round_list.extend(C)
        round_list.extend(D)
        round_list.extend(E)

        #créer la liste qui rassemble les différents mots




    # print(list[0:len(list)])

    #Choisir son personnage :

        Joueur_2="Joueur 2"

        Justin_Bieber="Justin"
        JUL="JUL"
        Six9ine="Six9ine"
        Lil_Pump="Lil_Pump"

        Persos=[
        Justin_Bieber,
        JUL,
        Six9ine,
        Lil_Pump]

        print(Persos)

        Personnage_Joueur1=[]
        Personnage_Joueur2=[]

        #choissisez votre personnage
        Choix_perso1=input("Joueur 1 Choissisez votre perso, 0 Justin Bieber, 1 Jul, 2 Six9ine, 3 Lil Pump ")
        #transformation du string en int pour l'indexisation de la liste Persos
        Choix_perso1=int(Choix_perso1)
        #Ajouter le choix a la liste perso du joueur 1
        Personnage_Joueur1.append(Persos[Choix_perso1])


        #Définir une classe au joueur 2 du coup, un point fort
        Joueur1.force=Persos[Choix_perso1]
        print("vous etes", Joueur1.force)




        del Persos[Choix_perso1]

        Choix_perso2=input("Joueur 2,  Choissisez votre perso, 0 Justin Bieber, 1 Jul, 2 Six9ine, 3 Lil Pump ")
        Choix_perso2=int(Choix_perso1)
        Personnage_Joueur2.append(Persos[Choix_perso2])
        print("\n")


        Joueur2.force=Persos[Choix_perso2]
        print("vous etes", Joueur2.force)
        print("\n")

        for x in range(len(round_list)):
            print (round_list[x].orthographe)


        #choisir dans la liste
        #choisir supprime
        #utiliser l'index pour choisir les mots que l'on veut
        #boucle liste vide
        #une fonction try pass a ete ajouté pour que taper un nombre hors du champ ne gene pas le jeu
        #mais il faut que cela permette de relancer le tour du joueur 1


        liste_joueur1 = []
        liste_joueur2 = []
        i=0
        Joueur_1Pts=0
        Joueur_2Pts=0
        phrase_finale1=[]
        phrase_finale2=[]

#indent au dessus vers la droite

        while i!=len(round_list):


            #créer juste un user input
            I=input("Joueur 1 Tapez l'index du mot a choisir(liste en haut")
            I=int(I)







            try:
                liste_joueur1.append(round_list[I])
                #c'est juste pour print mais ca print une adresse mémoir
                # print(liste_joueur1[0].orthographe)
            except IndexError:
                pass
            #supprime le mot choisi de la liste
            try:
                del round_list[I]
            except IndexError:
                pass


            # print("test1")
            for x in range(len(round_list)):
                print(round_list[x].orthographe)

            for x in range(len(liste_joueur1)):

                print(liste_joueur1[x].orthographe, end  =' ')







            #Mettre en place le joueur 2

                # créer juste un user input joueur 2
            print("\n")
            F = input("Joueur 2 Tapez l'index du mot a choisir(liste en haut)")
            F = int(F)



            # liste du joueur 2 en dessous
            try:
                liste_joueur2.append(round_list[F])

                #print du mot choisi seulement
                # print("",liste_joueur2[0].orthographe,end = ' ')

            except IndexError:
                pass

            # supprime le mot choisi de la liste
            try:
                del round_list[F]
            except IndexError:
                pass


            #print chaque element de la round list
            for x in range(len(round_list)):
                print(round_list[x].orthographe)

            # print la phrase du joueur 2
            for x in range(len(liste_joueur2)):
                # print("\n")
                # print("Le joueur 2 dit")
                # print(liste_joueur2[x].orthographe, end=' ' )
                print(liste_joueur2[x].orthographe,end =' ')

                # print("nombre liste joueur 2",len(liste_joueur2))




        #

        #CONDICTIONS VICTOIRES JOUEUR 1

        #si la phrase suit l'ordre exemple verbe+sujet+alors c'est bon
        #mettre les variables etc :
            if len(liste_joueur1)==3:
                if liste_joueur1[0].grammaire=="sujet" and liste_joueur1[1].grammaire=="verbe" and liste_joueur1[2].grammaire=="mot commun":
                # elif
        #afficher la phrase
                    print(liste_joueur1)

                    print("Bonne phrase")
        #attribuer le point
                    Joueur_1Pts +=5

                    print(Joueur_1Pts)
        #multiplier les points si la liste du joueur 1 contient un element force qui correspond au joueur 2
            #
                else:
                    print("\n")
                    print("Mauvaise phrase Joueur 1")
                    Joueur_1Pts -= 5
                    print(Joueur_1Pts)

                    liste_joueur1 = []

                try:
                    for x in range(len(liste_joueur1)):

                        if liste_joueur1[0].force == Joueur2.force:
                            del liste_joueur1[0]

                            Joueur_1Pts = Joueur_1Pts * 2
                            print(Joueur_1Pts)

                            print("Combo!")
                        else:
                            del liste_joueur1[0]
                            #pour savoir que cette commande marche
                            print("\n")
                            print("ce mot n'est pas un combo")
                except IndexError:
                    pass



            #vider la liste, definir comme vide

                    liste_joueur1=[]




        #CONDITIONS VICTOIRE JOUEUR 2:

            if len(liste_joueur2)==3:
                if liste_joueur2[0].grammaire=="sujet" and liste_joueur2[1].grammaire=="verbe" and liste_joueur2[2].grammaire=="mot commun":
        #afficher la phrase

                    print(liste_joueur2)
                    print("\n")
                    print("Bonne phrase")
        #attribuer le point
                    Joueur_2Pts +=5
                    print(Joueur_2Pts)
        #vider la liste, definir comme vide
                    print("Test reset")
                    liste_joueur2=[]
                try:
                    for x in range(len(liste_joueur1)):

                        if liste_joueur2[0].force == Joueur1.force:
                            del liste_joueur2[0]
                            Joueur_2Pts = Joueur_2Pts * 2
                            print("\n")
                            print(Joueur_2Pts)

                            print("Combo!")
                        else:
                            del liste_joueur2[0]
                            # pour savoir que cette commande marche
                            print("\n")
                            print("ce mot n'est pas un combo")
                except IndexError:
                    pass
                else :

                    print("Mauvaise phrase Joueur 2")
                    Joueur_2Pts -=5
                    print("\n")
                    print(Joueur_2Pts)
                    liste_joueur2=[]



                #faire une phrase complete:
                #autant extend une liste en faite :
                # liste_joueur1=str(liste_joueur1[x].orthographe)
                # print(liste_joueur1)
                # phrase_joueur1= ' '.join(liste_joueur1)
                # print(phrase_joueur1)

    #annonce du vainqueur à la fin:

        if Joueur_1Pts>Joueur_2Pts:
            print(Joueur1.force,"a clashé violemment",Joueur2.force)
        else:
            print(Joueur2.force,"a clashé violemment",Joueur1.force)

        jouer = input("Voulez vous recommencer (y/n)").lower()



print("Vous avez quitté le jeu")


    #bouton pour recommencer le jeu lancer le jeu
    #bouton pour quitter le jeu : input

