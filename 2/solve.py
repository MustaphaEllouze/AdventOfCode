# J'ouvre et je lis mon fichier
fic = open('input.txt')
lignes = fic.readlines()
fic.close()     # Et je n'oublie pas de le ferme

# Mettre True si on veut la premiere partie de l'enigme
# False si on veut la deuxieme partie
partie_1 = False

# C'est mon score initial que j'incremente a chaque match
mon_score = 0

# Pour chaque partie jouee (ligne de mon input)
for ligne in lignes:

    # Je recupere la ligne et j'enleve le caractere de fin de ligne
    ligne_traitee = ligne.strip()

    # Je separe la ligne en deux au niveau de l'espace
    ligne_traitee = ligne_traitee.split()

    # Mon adversaire a joue le premier caractere lu
    signe_adversaire = ligne_traitee[0]

    # J'ai joue le deuxieme caractere lu
    mon_signe = ligne_traitee[1]


    if(partie_1):       # Premiere enigme

        # Matchs possibles : 
        #                    X(Pierre)   Y(Feuille)   Z(Ciseaux)
        #  A(Pierre)         3+1          6+2           0+3
        #  B(Feuille)        0+1          3+2           6+3
        #  C(Ciseaux)        6+1          0+2           3+3

        # J'ecris tous les matchs possibles a la main
        # Et j'incremente mon score en fonction
        if(signe_adversaire=='A'):
            if(mon_signe=='X'):
                mon_score += 3+1
            elif(mon_signe=='Y'):
                mon_score += 6+2
            elif(mon_signe=='Z'):
                mon_score += 0+3
        elif(signe_adversaire=='B'):
            if(mon_signe=='X'):
                mon_score += 0+1
            elif(mon_signe=='Y'):
                mon_score += 3+2
            elif(mon_signe=='Z'):
                mon_score += 6+3
        elif(signe_adversaire=='C'):
            if(mon_signe=='X'):
                mon_score += 6+1
            elif(mon_signe=='Y'):
                mon_score += 0+2
            elif(mon_signe=='Z'):
                mon_score += 3+3
    
    else:

        # Matchs possibles : 
        #                    X(perd)     Y(egal)    Z(gagne)
        #  A(Pierre)         0+3          3+1           6+2
        #  B(Feuille)        0+1          3+2           6+3
        #  C(Ciseaux)        0+2          3+3           6+1

        # J'ecris tous les matchs possibles a la main
        # Et j'incremente mon score en fonction
        if(signe_adversaire=='A'):
            if(mon_signe=='X'):
                mon_score += 0+3
            elif(mon_signe=='Y'):
                mon_score += 3+1
            elif(mon_signe=='Z'):
                mon_score += 6+2
        elif(signe_adversaire=='B'):
            if(mon_signe=='X'):
                mon_score += 0+1
            elif(mon_signe=='Y'):
                mon_score += 3+2
            elif(mon_signe=='Z'):
                mon_score += 6+3
        elif(signe_adversaire=='C'):
            if(mon_signe=='X'):
                mon_score += 0+2
            elif(mon_signe=='Y'):
                mon_score += 3+3
            elif(mon_signe=='Z'):
                mon_score += 6+1

# J'imprime mon score
print('Mon score = ' + str(mon_score))
