# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 17:48:48 2020

@author: Jhulissa Villamagua
"""

import pandas as pd

df = pd.DataFrame()
def _loadCsv():
  global df
  df = pd.read_csv('computación_1.csv')
_loadCsv()
df.shape

dfaux = df.copy(deep = True)

df.pop('estado_asignatura')
df.pop('asignatura')    
df.pop('nota_ingresada')
#df.pop('carrera')

#print(dfaux.asignatura.unique().tolist())
colums = df.columns.tolist() +['PERDIDAS']+ dfaux.asignatura.unique().tolist()

dff = pd.DataFrame(columns=colums)



for cedula in dfaux.cedula.unique():
    
    perdidas = 0
    lvlciclo = 0
    
    estudiante = dfaux.loc[dfaux['cedula']==cedula].copy()
    
    #dataux=estudiante.iloc[0][0:8]
    dataux=estudiante.iloc[0][0:len(df.columns)]
    
    #dt = dataux.tolist()
    #dt = dt + list(range(100,len(dfaux.asignatura.unique().tolist())+101))
    dt = dataux.tolist()
    dt = dt + list(range(100,len(dfaux.asignatura.unique().tolist())+101))
    dff.loc[len(dff)] = dt
    #print(len(dt))
    #print(len(dff.columns))
    #dff.loc[len(dff)] = dt
    
    for asignatura in estudiante.asignatura.unique():
       dff.loc[dff['cedula']==cedula, [asignatura]] = estudiante.loc[estudiante['asignatura']==asignatura].estado_asignatura.values[0]
       
       if lvlciclo < estudiante.loc[estudiante['asignatura']==asignatura].ciclo.values[0]: 
           lvlciclo = estudiante.loc[estudiante['asignatura']==asignatura].ciclo.values[0]

       if estudiante.loc[estudiante['asignatura']==asignatura].estado_asignatura.values[0] == 0:
           perdidas = perdidas + 1
          
            
    
    dff.loc[dff['cedula']==cedula,['PERDIDAS']] = perdidas
    dff.loc[dff['cedula']==cedula,['ciclo']] = lvlciclo

dff = dff.replace(list(range(100,len(dfaux.asignatura.unique().tolist())+101)),2)   

print(dfaux.asignatura.unique().tolist())
for asignatura in dfaux.asignatura.unique().tolist():
    dff.loc[dff[asignatura]==2,[asignatura]] = round(dff[asignatura].mean())

#print(dff)
##dff.loc[dff['']]

dff.to_csv('compu_4_filtro.csv')

    







