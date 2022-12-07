# Classe representant un dossier
# * dirs : liste des instances (i.e. tous les dossiers)
# * names : liste des noms (pour etre surs que l'input ne parcourt pas plusieurs fois le meme dossier)
class directory :
    dirs = []
    names = []

    
    def __init__(self,name,parent,children=None):
        """Constructeur de la classe

        Args:
            name (str): nom du dossier
            parent (directory): nom du dossier parent
            children (directory or file): liste des enfants de ce dossier

        """
        # On rajoute une Exception si on a deja parcouru ce dossier dans l'input 
        # (en l'occurrence l'enonce ne le dit pas, mais ca n'arrive jamais)
        if name in directory.names:
            raise Exception()
        
        # Attribut name
        self.name = name

        # Attribut parent
        self.parent =parent

        # On met a jour les children du dossier parent ici
        if(not parent is None):
            self.parent.children.append(self)
        if(children is None):
            self.children = []
        else:
            self.children = children
        
        # La taille du dossier (calcule avec size_func)
        self.size = None

        # On stocke l'instance dans directory.dirs pour pouvoir la recuperer plus tard
        directory.dirs.append(self)


    def size_func(self):
        """"
        Retourne la taille du dossier
        """
        # Si on l'a deja calcule, on renvoit ce qui a stocke dans self.size
        # Note: cela permet de ne pas faire exploser le temps de calcul
        #       pour une arborescence trop grande
        if(not self.size is None):
            return self.size
        # Sinon on ne l'a pas deja calcule
        else:
            s=0 
            # On parcourt les enfants, et on somme leur taille
            for child in self.children:
                if(type(child) is directory):
                    s+=child.size_func()
                else:
                    s+=child.size
            #On met a jour l'attribut self.size pour pouvoir esperer un jour 
            # tomber dans le if au-dessus
            self.size=s
            #Et on renvoie la variable qu'on a calcule
            return s

# Classe qui represente un fichier
# * files : idem que dirs (cf. au-dessus)
# * names : idem que names (cf. au-dessus)
# Note MEE : On aurait pu faire mieux en traitant les dossiers et les fichiers
#           avec la meme classe (en disant par exemple que les dossier sont des
#           fichiers de taille nulle et en autorisant les files d'avoir des 
#           enfants), mais c'est plus clair de tout distinguer
class file :
    files = []
    names = []

    def __init__(self,name,parent,size):
        """Constructeur de classe

        Args:
            name (str): nom du fichier
            parent (directory): dossier parent
            size (int): taille du fichier

        """
        # Idem, gestion d'exception
        if name in file.names:
            raise Exception()
        
        # Attributs
        self.name = name
        self.parent = parent
        self.size = size
        
        # On met a jour l'attribut children du dossier parent
        self.parent.children.append(self)

        # On range les fichiers dans file.files pour pouvoir les extraire facilement
        file.files.append(self)

# On lit l'input
fic = open('input.txt','r')
lines = fic.readlines()
fic.close()

doss_courant = None     # Le dossier dans lequel on est
flag_ls = False         # Si on est dans la lecture du resultat d'un ls

# Pour chaque ligne apparaissant dans le terminal
for line in lines:
    l = line.strip()                                                # On enleve le caractere de fin de ligne
    if('$' in l):                                                   # Si on lit une commande
        flag_ls = False                                             # On est pas dans la description d'un ls
        if('$ cd ' in l):                                           # Si la commande est un 'cd'
            nom_doss = l.split(' cd ')[-1]                          # On recupere le nom du dossier (potentiellement '..')
            if(not '..' in nom_doss):                               # Si on doit cree un nouveau dossier
                doss_courant = directory(nom_doss,doss_courant,None)# On utilise la classe qu'on le fait, et on dit que le dossier parent est le dossier courant
            else:                                                   # Si on doit remonter d'un cran
                doss_courant = doss_courant.parent                  # On appelle le parent du dossier courant
        elif('$ ls' in l):                                          # Si la commande est un ls
            flag_ls = True                                          # On dit que les prochaines lignes correspondent a la lecture d'un ls
    elif(flag_ls):                                                  # Si on est en train de lire le contenu d'un dossier
        if('dir ' in l):                                            # Si on tombe sur un dossier
            pass                                                    # On ne fait rien (Note MEE : J'ai fait l'hypothese qu'on parcourait tous les dossiers dans l'input)
                                                                    # (dans le cas general, bien sur, ca ne marcherait pas si bien)
        else:                                                       # Sinon, si c'est un fichier
            ll = l.split()                                          # On recupere nos infomations
            file(ll[1],doss_courant,int(ll[0]))                     # Et on cree un fichier dans le dossier courant

#
#   A partir de ce point, on a tout ce qu'il faut pour resoudre notre enigme
#   Les algorithmes sont relativement simples car tout a deja ete encapsule 
#   au-dessus ! :)
#

# Partie 1 
resultat_enigme_1 = sum([dir.size_func() for dir in directory.dirs if dir.size_func()<100000])
print('Enigme 1 : ' + str(resultat_enigme_1))

# Partie 2
free_space_to_find = 30000000-(70000000-directory.dirs[0].size_func())               # Espace a liberer
resultat_enigme_2 = 70000000                                                         # Contient la plus petite taille trouvee
for dir in directory.dirs:                                                           # Pour chaque dossier
    if(dir.size_func()>free_space_to_find and dir.size_func()<resultat_enigme_2):    # Si on trouve un dossier plus petit qui est une solution au probleme
        resultat_enigme_2 = dir.size_func()                                          # On retient sa taille

print('Enigme 2 : ' + str(resultat_enigme_2))
