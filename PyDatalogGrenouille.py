# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 10:49:15 2019

@author: Moi
"""

from pyDatalog import pyDatalog

pyDatalog.clear() #Reset le log
pyDatalog.create_terms('croakes, eatFlies, frog, canary, chirps, sings, green, yellow')

+ croakes("fritz")
+ eatFlies("fritz")
+ croakes("Boi")
+ eatFlies("Boi")
+ croakes("Gif")
+ eatFlies("Gif")
+ eatFlies("Criss")


pyDatalog.load("""
    frog(X) <= croakes(X) & eatFlies(X)
    canary(X) <= sings(X) & chirps(X)
    green(X) <= frog(X)
    yellow(X) <= canary(X)
              """)

print(pyDatalog.ask("green('fritz')"))