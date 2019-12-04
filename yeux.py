# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 14:27:29 2019

@author: Corentin
"""

from pyDatalog import pyDatalog
import pandas

#Reset le log
pyDatalog.clear() 

#Lecture du CSV
df = pandas.read_excel('Data/yeux.xlsx',sheet_name='Symptomes', names=['colA', 'colB'], header=None, )

#Formatage des termes
df_selected = df['colA'].values
df = pandas.DataFrame(df_selected)
df2 = df.to_csv(header=None, index = False).strip('\r\n').split('\r\n')
df3 =','.join(df2).lower()

#Print verification des termes
#print (df3)

#Importation des termes dans Pydatalog
pyDatalog.create_terms(df3)


#Récuperation des regles WORK IN PROGRESS (J'arrive pas a formater, 
#je fais en dur pour le moment)

#df = pandas.read_excel('Data/yeux.xlsx',sheet_name='Règles', names=['colA'], header=None, )
#
#df_selected = df['colA'].values
#df = pandas.DataFrame(df_selected)
#df2 = df.to_csv(header=None, index = False)
#
##df3 =df2.replace(',"','')
##df3= df3.replace('"','')
##df3= df3.replace('\'','')
##d= df3.replace(';','')
##df3=df3.replace('(','[')
##df3=df3.replace(')',']')
##df3 =','.join(df2).lower()
#
#print (df2[2])

#Faits

+ g001("malade1")
+ g002("malade1")
+ g003("malade1")
+ g004("malade1")
+ g005("malade2")
+ g006("malade2")

#Regles importé en brut

pyDatalog.load("""
    p01(X) <= g001(X) & g002(X) & g003(X) & g004(X)
    p02(X) <= g001(X) & g002(X) & g005(X) & g006(X)
    p03(X) <= g007(X) & g008(X)
    p04(X) <= g009(X) & g010(X) & g011(X) & g012(X)
    p05(X) <= g013(X) & g014(X) & g015(X) & g016(X)
    p06(X) <= g010(X) & g015(X) & g016(X) & g017(X) & g018(X) & g019(X)
    p07(X) <= g0010(X) & g019(X) & g020(X) & g021(X)
    p08(X) <= g001(X) & g010(X) & g019(X) & g022(X) & g023(X)
              """)

print(pyDatalog.ask("p01(X)"))
print(pyDatalog.ask("p02(X)"))