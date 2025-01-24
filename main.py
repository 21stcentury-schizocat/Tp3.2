"""""
Liam Rodriguez
2024-10-15
Monster fight
"""""

niveau_vie = 20
import random

boss_fight = False
boss_counter = 0
roll = True
game = True

print("Vous vous trouvé dans un couloir")
print("Il y a plusieurs porte avec des monstres derriere eux")
print("Vous ouvrez une de ces portes")


while game:
    if boss_fight:
        print("Vous recontrer un gros monster, que si vous countournerez vous perderez un point de vie et devrais encore \n combatre le monstre")

        monstre = random.randint(3,5)
    else:
        monstre = random.randint(1,5)
        print(f"Vous tombez face à face avec un adversaire de difficulté:{monstre}")

    print("Que voulez-vous faire ? \n 1- Combattre cet adversaire\n 2- Contourner cet adversaire et aller ouvrir une autre porte")
    reponse = int(input(" 3- Afficher les règles du jeu \n 4- Quitter la partie"))

    if reponse == 1:
        print("Vous essayer de combatre le monstre")
        de = random.randint(1,6)
        if de > monstre:
            print(f"vous vainquer le monstre avec un {de}")
            niveau_vie += monstre
            print(f"Il vous reste {niveau_vie} points de vies")
            boss_counter += 1
            if boss_counter % 3 == 0:
                boss_fight = True


        else:
            print(f"vous essayer de combatre le monstre avec un {de}")
            print(f"Vous etes vaincu et perdez {monstre} point de vies")
            niveau_vie -= monstre
            print(f"Il vous reste {niveau_vie}")
            if niveau_vie <= 0:
                print("vous etes mort :C")
                exit()
            else:
                game = True
    elif reponse == 2:
        print("Vous contournez le monstre et ouvrez une autre porte")
        niveau_vie -= 1
        print(f"Il vous reste {niveau_vie} points de vie")
        if niveau_vie <= 0:
            print("vous etes mort :C")
            exit()
        else:
            game = True

    elif reponse == 3:
        print("Pour réussir un combat, il faut que la valuer du dé soit supérieure a la force du monstre.")
        print("Dans ce cas, le niveau de vie de l'usager est augmenté de la force de l'adversaire.")
        print("Une défaite a lieu lorsque le dé lancé par l'usager est inférieure ou égale a la force du monstre.")
        print("Dans ce cas, le niveau de vie de l'usager est diminué de la force de l'adversaire.")
        print("La partie se termine lorsque les points de vie de l'usager tombent sous 0.")
        print("L'usager peut combattre ou éviter chaque adversaire, quand vous évitez, vous perdez 1 point de vie.")
    elif reponse == 4:
        print("Merci d'avoir jouer :)")
        game = False
