# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""
import sys  

from easygui import multenterbox
from easygui import read_or_create_settings
from easygui import integerbox
from easygui import boolbox
from easygui import choicebox
from easygui import multchoicebox
from easygui import textbox
#import pprint

ingredients = ["tomate", "mozzarella", "jambon",
               "champignons", "salami piquant",
               "basilic","anchois","câpres","crème",
               "chèvre","Emmental & Fourme d'Ambert AOP",
               "ananas","artichaut", "olives", "huile d'olive"]

msg= "Entrez vos coordonnées"
title= "Données"
fields= ("Nom", "Prenom", "Tel", "Mail")
mes_choix = multenterbox(msg,title,fields)

settings = read_or_create_settings("Client.txt")
settings.prenomClient = mes_choix[0]
settings.nomClient = mes_choix[1]
settings.numTelClient = mes_choix[2]
settings.mailClient = mes_choix[3]

title = "Nombre de Pizza"
min = 1
max = 100
defaut = 1
msg="Nombre de Pizzas à commander [{} .. {}]".format(min,max)
nbPizzaClient = integerbox(msg,title,defaut,min,max)
settings.nbPizza = nbPizzaClient

pizzas ={}
for i in range(0,nbPizzaClient):
    
    message = "Voulez vous une pizza predefinie ?"
    title = "Choix pizza"
    if boolbox(message, ("Oui","Non")):
        msg = "Quelle Pizza ?"
        title = "Choix Pizza"
        choices = ("Reine","Diavola","Sicilienne","Quatre Fromages","Hawaienne",
                   "Capricciosa")
        choice = choicebox(msg, title, choices)
        pizzas[i]=choice
    else:
        custom = {}
        msg = "Quelles ingredients ?"
        title = "Choix Pizza"
        choices = ingredients
        choice = multchoicebox(msg, title, choices)
        pizzas[i]=choice
        
        
settings.prix = len(pizzas)*10
settings.pizzas = pizzas
settings.store()

msg = "Résumé de commande"
title = "Ticket"
text = settings.prenomClient +" "+ settings.nomClient + "\n" + settings.numTelClient + "\n" + settings.mailClient 
for i in range(len(pizzas)):
    text += " \n" + str(pizzas[i])
text += "\n TOTAL :" + str(settings.prix) + " EUROS"
textbox(msg,title,text)