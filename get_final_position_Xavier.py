# -*- coding:utf8 -*-
"""Script permettant de localiser le robot B-VZXR en fonction de deux fichiers txt"""
################################################################################
# fichier  : get_final_position_Xavier.py
# Auteur : LAI Xavier
################################################################################

################################################################################
# Importation de fonctions externes :
import turtle

# Definition locale de fonctions :
def get_final_position(fichier_instruction,fichier_univers):
    
    #On utilise un objet turtle et on le rend rapide.
    robot = turtle.Turtle()
    robot.reset()
    robot.speed('fastest')
    turtle.tracer(False)
    robot.hideturtle()
    
    #La tête du robot doit être vers le haut dans R².
    robot.left(angle=90)

    #On va chercher les dimensions de l'espace cartésien.
    with open(fichier_univers,'r') as u:
        lignes_u = u.readlines()
        width = int(lignes_u[0].split(': ')[1])
        height = int(lignes_u[1].split(': ')[1])
    
    #On lit chaque instruction pour en déterminer la direction et le pas.
    with open(fichier_instruction,'r') as f:
        lignes = f.readlines()
        for ligne in lignes:
            instructions = ligne.split(', ')
            direction,pas = instructions[0],int(instructions[1])
            
            #On tourne le robot à droite ou à gauche selon l'instruction
            if direction == 'right':
                robot.right(angle=90)
            else:
                robot.left(angle=90)
            
            #On avance le robot de 'pas' cases
            robot.forward(pas)
            
            #La position après l'avancement du robot
            pos = robot.pos()
            
            #On veut que le robot reste sur le bord lorsqu'il dépasse l'espace cartésien
            if pos[0] < 0:
                robot.setpos(0,pos[1]) #setpos pour repositionner
            elif pos[0]> width:
                robot.setpos(width,pos[1])
            elif pos[1] < 0:
                robot.setpos(pos[0],0)
            elif pos[1]>height:
                robot.setpos(pos[0],height)
            
        print("\n --------- Position finale du robot --------\n\t\t",robot.pos())


################################################################################
# Corps principal du programme :

fichier_instruction = "instrucion_list.txt"
fichier_dimension = "universe.txt"

get_final_position(fichier_instruction,fichier_dimension)
    
