# Enigme 6 - MEE

# Lecture du fichier
fic = open('input.txt','r')
lines = fic.readlines()
fic.close()

# On recupere la ligne sans le caractere de fin de ligne
line = lines[0].strip()

# Longueur du buffer
long = 14

# Initialisation
buffer = [' ']*long

# On parcourt le caractere
for i,c in enumerate(line):
    # On rempalce la derniere letrte dans le buffer par le caractere lu
    buffer[i%long] = c
    # Condition d'arret : tous les caracteres doivent etre differents
    # On s'arrete si on a True partout
    checker = [buffer[ii] != buffer[jj] for ii in range(len(buffer)) for jj in range(ii+1,len(buffer))]
    # Arret et print de la solution
    if(all(checker) and i>=long):
        print('Solution = ' + str(i+1))
        break