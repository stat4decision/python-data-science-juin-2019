# -*- coding: utf-8 -*-
"""
Ce module contient une fonction de moyenne de listes
"""

def moyenne_listes(l1,l2):
    """ Cette fonction calcule la moyenne des éléments de deux listes """
    somme = 0
    for val in l1+l2:
        somme = somme + val    

    return somme / len(l1+l2)