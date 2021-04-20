import sys
import os
from time import sleep
from random import randint
from carte import *
from monstre import *
from master import *
screen_width = 100



####################################################
# Fonctions du menu :
def Menu():
  Title()
  print("                                       --------------------------------")
  print("                                             1: Nouvelle partie")
  print("                                             2: Charger partie")
  print("                                             3: Credits")
  print("                                             4: Quitter")
  print("                                        -------------------------------")
  Choix = int(input(">"))
  if Choix == 1:
    LancerLeJeux()
  elif Choix == 2:
    ChargerPartie()
  elif Choix == 3:
    Credits()
  else:
    sys.exit()

def LancerLeJeux():
      cls()
      print("\nQu'elle est ton nom jeune guerrier ?\n")
      joueur1.nom = Pseudo()
      print("\nTu a une tête bizarre , Tu viens d'ou ?")
      joueur1.position = choixpays()
      jeupasfini()

def ChargerPartie():
  print("TODO chargerpartir")
  Menu()


def Credits():
  print("Notre jeux ce compose d'un monde à 3 plateformes qui sont 3 pays avec dans chacun d'eux 16 levels que tu pourras\ndécouvrir comme bon te semble.\nTu pourras te déplacer dans chaque map par haut bas gauche droite et les cartes sont reliés par des ports.\nObjectif combattre le big boss final,\n tu devras avant de le combattre trouver les enigmes cachés de Yashin, 1 pour chaque pays énigmes et loot t'attendent.\n Oui un bon jeux à l'ancienne.\nPour les actions, très simple il te suffira de taper l'action proposer et ENTER et te laisser guider par le jeux.\n Tu a la possibilité de revenir sur tes pas et combattre le même monstre.")
  Menu()

def jeupasfini():
  print("")
  print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
  print("Que veux-tu faire?\n")
  AffichageAction()
  action = input("\n> ")
  acceptable_actions = ["aller", "combat", "parler" ,"fuir", "save", "quit"]
  while action.lower() not in acceptable_actions:
    print("Action inconnue, Essaye encore.\n")
    action = input("> ")
  if action.lower() in ["aller"]:
    move(action.lower())
  elif action.lower() in ["combat"]:
    Event()
  elif action.lower() in ["fuir"]:
    move(action.lower())
  elif action.lower() in ["parler"]:
    master()
  elif action.lower() in ["save"] or action.lower() in ["quit"]:
    save()
    Menu()
        
def combatWin():
      print("")
      print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
      print("Que veux-tu faire?\n")
      print("aller")
      print("save")
      action = input("\n> ")
      acceptable_actions = ["aller",  "save", "quit"]
      while action.lower() not in acceptable_actions:
        print("Action inconnue, Essaye encore.\n")
        action = input("> ")
      if action.lower() in ["aller"]:
        move(action.lower())
      elif action.lower() in ["save"] or action.lower() in ["quit"]:
        save()
        Menu()

def save():
  print("save")

def AffichageAction ():
      if carte[joueur1.position][ACTION] == "combat":
            print("\n", monstre[joueur1.position][NOM], "vient d'apparaitre devant toi!")
            print("Il a", monstre[joueur1.position][HP], "de vie.\n")
            print("\nTu a", joueur1.HP, " de vie !")
            print("combat")
            print("fuir")
            print("save")
      elif carte[joueur1.position][ACTION] == "maitre":
            print("\nUn homme mysterieu s'avance devant toi.\n")
            print("parler")
            print("aller")
            print("save")
      else:
            print("aller")
            print("save")  
      
def GameOver():
      print("\nGAME OVER !\n")
      Menu()

def fini():
      print("\nFélicitation,\n tu a passé avec succès tous les périples de la quête de Yan Shin\n Il est temps pour toi d'enseigner ce que tu a appris et devenir le nouveau maître du temple")
      Menu()

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

###########################################################################
# Fonction de l'exploration :

def print_location():
    cls()
    	# info de la position du joueur
    print("\n" + ("#" * (4 +len(joueur1.position))))
    print("# " + joueur1.position.upper() + " #")
    print("#" * (4 +len(joueur1.position)))
    print("\n" + (carte[joueur1.position][DESCRIPTION]))
    jeupasfini()

def move(myAction):
  print("\nhaut   ->   " + (carte[joueur1.position][HAUT] ))
  print("bas      ->   " + (carte[joueur1.position][BAS] ))
  print("gauche   ->   " + (carte[joueur1.position][GAUCHE] ))
  print("droite   ->   " + (carte[joueur1.position][DROITE] ))

  askString = "\nOu veux-tu "+myAction+"?\n> "
  destination = input(askString)
  if destination == "haut":
    move_dest = carte[joueur1.position][HAUT]
    if move_dest == "ravin" or move_dest == "océan":
      print("tu va dans le mur")
      print("choisi un autre chemin.")
      move(myAction) 
    move_player(move_dest)   
  elif destination == "gauche":
    move_dest = carte[joueur1.position][GAUCHE]
    if move_dest == "ravin" or move_dest == "océan":
      print("tu va dans le mur")
      print("choisi un autre chemin.")
      move(myAction)
    move_player(move_dest)
  elif destination == "droite":
    move_dest = carte[joueur1.position][DROITE]
    if move_dest == "ravin" or move_dest == "océan":
      print("tu va dans le mur")
      print("choisi un autre chemin.")
      move(myAction)
    move_player(move_dest)
  elif destination == "bas":
    move_dest = carte[joueur1.position][BAS]
    if move_dest == "ravin" or move_dest == "océan":
      print("tu va dans le mur")
      print("choisi un autre chemin.")
      move(myAction)
    move_player(move_dest)
  else:
    print("Je ne comprend pas, essaye haut, bas, gauche, ou droite.\n")
    move(myAction)

def move_player(move_dest):
	joueur1.position = move_dest
	print_location()

###########################################################################
# fonction de l'action ou item :


def Event():
  DeChoix = De10()
  if DeChoix <= 7:
      bonus = choixItem()
      Combat()
  else:
      Item()

def Combat():
      hpm = monstre[joueur1.position][HP]
      First = FirstBlood()
      i = 1
      while monstre[joueur1.position][HP] > 0:
                  if First == True:
                        print("\nTour",i)
                        DeDeff = De10()
                        if DeDeff >= 7:
                              print(monstre[joueur1.position][NOM], "a esquivé votre attaque.")
                        else:
                              monstre[joueur1.position][HP] = (monstre[joueur1.position][HP] + monstre[joueur1.position][ATT]) - (joueur1.ATTAQUE + joueur1.ARME[4])
                              print(monstre[joueur1.position][NOM],"a subi",(joueur1.ATTAQUE + monstre[joueur1.position][RECOMPENSE][4]), "de dégâts.")
                        DeDeff = De10()
                        if DeDeff >= 6:
                              print("Vous avez esquivé l'attaque.")
                        else:
                              joueur1.HP = (joueur1.HP + joueur1.DEFENSE + joueur1.ARME[3]) - monstre[joueur1.position][ATT]
                              print("Vous avez subi", monstre[joueur1.position][ATT], "de dégâts.")
                        print("Il te reste", joueur1.HP, "de vie.")
                        print("Il reste", monstre[joueur1.position][HP], "au", monstre[joueur1.position][NOM])
                        if monstre[joueur1.position][HP] <= 0:
                              monstre[joueur1.position][HP] = hpm
                              joueur1.HP = joueur1.HP + 20
                              if monstre["Boss"][HP] <= 0:
                                    fini()
                              else:
                                    Win()
                                    combatWin()
                        elif joueur1.HP <= 0:
                              GameOver()
                  else:
                        print("\nTour",i)
                        DeDeff = De10()
                        if DeDeff >= 6:
                              print("Vous avez esquivé l'attaque.")
                        else:
                              joueur1.HP = (joueur1.HP + joueur1.DEFENSE + joueur1.ARME[3]) - monstre[joueur1.position][ATT]
                              print("Vous avez subi", monstre[joueur1.position][ATT], "de dégâts.")
                        DeDeff = De10()
                        if DeDeff >= 7:
                              print(monstre[joueur1.position][NOM], "a esquivé votre attaque.")
                        else:
                              monstre[joueur1.position][HP] = (monstre[joueur1.position][HP] + monstre[joueur1.position][ATT]) - (joueur1.ATTAQUE + joueur1.ARME[4])
                              print(monstre[joueur1.position][NOM],"a subi",joueur1.ATTAQUE, "de dégâts.")
                        print("Il te reste", joueur1.HP, "de vie.")
                        print("Il reste", monstre[joueur1.position][HP], "au", monstre[joueur1.position][NOM])
                        if monstre[joueur1.position][HP] <= 0:
                              monstre[joueur1.position][HP] = hpm
                              joueur1.HP = joueur1.HP + 20
                              if monstre["Boss"][HP] <= 0:
                                    fini()
                              else:
                                    Win()
                                    combatWin()
                        elif joueur1.HP <= 0:
                              GameOver()
                  i = i + 1                                                            

def FirstBlood():
      DeFirst = De10()
      if DeFirst <= 5:
            print("\nVous attaquez en premier")
            return True
      else:
            print("\nCe monstre est rapide, il a devancé ton attaque")
            return False

def Item():
  DeItem = De10()
  if DeItem <= 5:
        if len(joueur1.INVENTAIRE[0]) >= 2:
              print("Tu n'a plus de place pour ce type de Bonus!")
              combatWin()
        else:   
              print("Tu a gagné un bonus d'attaque.")
              joueur1.INVENTAIRE[0].append("Bonus d'Attaque")
  else:
        if len(joueur1.INVENTAIRE[1]) >= 2:
              print("Tu n'a plus de place pour ce type de Bonus!")
              combatWin()
        else:
              print("Tu a gagné un bonus de Defense.")
              joueur1.INVENTAIRE[1].append("Bonus de Defense")
  combatWin()

def choixItem():
      print("\nUtilisez un Bonus pour le combat ?")
      print("\n oui / non ")
      choixI = str(input("> "))
      if choixI == "oui" or choixI == "o":
            print("Tu a", len(joueur1.INVENTAIRE[0]), "Bonus d'Attaque.")
            print("Tu a", len(joueur1.INVENTAIRE[1]), "Bonus de Defense.")
            print("1 : Bonus d'Attaque.")
            print("2 : bonus de Defense")
            choixB = int(input())
            if choixB == 1:
                  if len(joueur1.INVENTAIRE[0]) == 0:
                        print("Pas de bonus")
                        Combat()
                  else:
                        joueur1.INVENTAIRE[0].pop()
                        joueur1.ATTAQUE = joueur1.ATTAQUE + 10
                        return "ATT"
            elif choixB == 2:
                  if len(joueur1.INVENTAIRE[1]) == 0:
                        print("Pas de bonus")
                        Combat()
                  else:
                        joueur1.INVENTAIRE[1].pop()
                        joueur1.DEFENSE = joueur1.DEFENSE + 20
                        return "DEF"
            else:
                  print("Je n'ai pas compris!")
                  choixB = int(input())
      elif choixI == "non" or choixI == "n":
            print("combat va commencer")
            Combat()
      else:
            print("Je n'ai pas compris, recommence")
            choixI = str(input())



def master():
      print(enigme[joueur1.position][HISTOIRE])
      print("\n")
      print(enigme[joueur1.position][QUESTION])
      print("\nQue va-tu répondre ?")
      for k in enigme[joueur1.position][REPONSE]:
            print(k)
      print("\nQue va-tu répondre, 1, 2 ou 3")
      reponse = int(input("\n>"))
      if reponse == 2:
            print("\nTu a bien répondu !")
            Win()
      else:
            print("\nTu na rien écouter, pars !")
            combatWin()


def De10():
  return randint(1,10)

def Win():
      print("\ngagné\n")
      print("Tu a gagné,", monstre[joueur1.position][RECOMPENSE][0])
      if monstre[joueur1.position][RECOMPENSE][1] > 0:
            print(monstre[joueur1.position][RECOMPENSE][0], "donne", monstre[joueur1.position][RECOMPENSE][1], "d'xp.")
      if monstre[joueur1.position][RECOMPENSE][2] > 0:
            print(monstre[joueur1.position][RECOMPENSE][0], "donne", monstre[joueur1.position][RECOMPENSE][2], "de vie.")
      if monstre[joueur1.position][RECOMPENSE][3] > 0:
            print(monstre[joueur1.position][RECOMPENSE][0], "donne", monstre[joueur1.position][RECOMPENSE][3], "de défense.")
      if monstre[joueur1.position][RECOMPENSE][4] > 0:
            print(monstre[joueur1.position][RECOMPENSE][0], "donne", monstre[joueur1.position][RECOMPENSE][4], "d'attaque.")
      print("\nVeux-tu garder cette récompense ?")
      print("\n oui / non ")
      choixI = str(input("> "))
      if choixI == "oui" or choixI == "o":
            if monstre[joueur1.position][RECOMPENSE][1] > 0:
                  joueur1.XP = joueur1.XP + monstre[joueur1.position][RECOMPENSE][1]
            else:
                  joueur1.ARME = monstre[joueur1.position][RECOMPENSE]
                  print(joueur1.ARME[0], "est désormais ton arme.")
                  combatWin()
      elif choixI == "non" or choixI == "n":
            combatWin()
      else:
            print("Je n'ai pas compris, recommence")
            choixI = str(input())


###########################################################################
# intro :

def Pseudo():
  Nom = str(input(">"))
  print("\nBienvenu", Nom)
  return Nom

def choixpays():
    print("\njapon, tapez 1")
    print("chine, tapez 2")
    print("indonésie, tapez 3\n")
    Pays = int(input(">"))
    if Pays == 1:
        print("\nFils Unique du plus grand de tout les samouraïs, \n cherche à devenir plus fort que son père et seul \n la quête vers le dieu yashin lui permettra d'y parvenir...\n") # depart A1
        print(carte["petit village de pecheur"][DESCRIPTION])
        return "petit village de pecheur"
    elif Pays == 2:
        print("\nEnfant orphelin de l'empire céleste,\n te voilà décidé à retrouver celui qui tua tes parents et toutes ta famille \n après des années d'entrainement te voilà pret avec un seul mot en bouche VENGEANCE\n")# depart B13
        print(carte["Grand village de Pêcheur"][DESCRIPTION])
        return "Grand village de Pêcheur"
    elif Pays == 3:
        print("\nLa seule chose que tu sais en te réveillant au beau milieu de ce village abndonné,\n n'est que ton nom et une voix te disant 'trouve Yashin et tu le saura' \n") # depart C16
        print(carte["Village de Pêcheur abandonné"][DESCRIPTION])
        return "Village de Pêcheur abandonné"
    else:
          print("\nTu n'a pas compris la question ????")
          print("\nJe t'ai demander d'ou tu viens !!!!")
          choixpays()

def Title():
    print("                    __     __      _____ _     _          ____                  _")   
    print("                    \ \   / /     / ____| |   (_)        / __ \                | |")  
    print("                     \ \_/ /_ _  | (___ | |__  _ _ __   | |  | |_   _  ___  ___| |_") 
    print("                      \   / _` |  \___ \| '_ \| | '_ \  | |  | | | | |/ _ \/ __| __|")
    print("                       | | (_| |  ____) | | | | | | | | | |__| | |_| |  __/\__ \ |_") 
    print("                       |_|\__,_| |_____/|_| |_|_|_| |_|  \___\_\\__,_|\___||___/\__|")
    print("")
    print("")
    print("                             .Crée par Jeremy Abdoelsomad et Charles Joubert.")
####################################################################################
# Attribut du joueur au depart:

class joueur:
    def __init__(self):
        self.nom = ""
        self.XP = 0
        self.HP = 100
        self.DEFENSE = 0
        self.ATTAQUE = 10
        self.position = ""
        self.INVENTAIRE = [[],[]]
        self.ARME = ["mains", 0, 0, 0, 0]
        self.won = False
joueur1 = joueur()


Menu()

