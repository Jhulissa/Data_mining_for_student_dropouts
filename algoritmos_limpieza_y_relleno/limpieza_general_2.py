# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 15:16:15 2021

@author: DETPC
"""

import pandas as pd
import datetime as dt

df = pd.DataFrame()
def _loadCsv():
  global df
  df = pd.read_csv('data_inicial_completa.csv')
_loadCsv()
df.shape

print(df.columns)

#carrera = 'IngenierIa en Sistemas' 
carrera = 'COMPUTACION'
#columnas_a_usar = ['cedula','periodo_lectivo','fecha_nacimiento','genero','estado_civil','etnia','sector_procedencia','trabaja','ciclo','estado_matricula','asignatura','estado_asignatura','nota_ingresada']
#mallas_a_usar = ['2007-2008','2008-2009','2009-2010','2010-2011','2011-2012']
#mallas_a_usar = ['2017-2018','2018-2019','2019-2020']

df.drop(df.loc[df['carrera']==carrera].index, inplace=True)

#for col in df.columns.tolist():
 #   if col not in columnas_a_usar:
#        df.pop(col)
    
print(df.carrera)

#df.drop(df.loc[df['estado_matricula'].str.lower()=='matriculada'].index,inplace=True)


#for mallas in mallas_a_usar:    
 #   for cedula in df.loc[df.periodo_lectivo==mallas].cedula.unique():
  #      df.drop(df.loc[df.cedula == cedula].index,inplace=True)
    #df.drop(df.loc[df['periodo_lectivo'].str.lower()==mallas].index,inplace=True)

df.drop(df.loc[(df.estado_asignatura.isnull()) & (df.nota_ingresada.isnull())].index,inplace=True)

df.loc[df.nota_ingresada < 7,'estado_asignatura'] = 'reprobada'

df.loc[(df.nota_ingresada >= 7) & (df.estado_asignatura == 'reprobada' ),'estado_asignatura'] = 'aprobada'

df.loc[(df.nota_ingresada >= 7) & (df.estado_asignatura.isnull()),'estado_asignatura'] = 'aprobada'

#********************************************************************
df.loc[(df.ingreso_estudiante > 0) ,'ingreso_estudiante'] = 1

df.loc[(df.ingreso_estudiante == 0) ,'ingreso_estudiante'] = 0
#********************************************************************
df.loc[(df.numero_hijos > 0),'numero_hijos'] = 1

df.loc[(df.numero_hijos == 0),'numero_hijos'] = 0


#df.loc[(df.estado_matricula.isnull()) & (df.estado_asignatura == 'homologada'),'estado_matricula'] = 'aprobada'
#df.loc[(df.estado_matricula.isnull()) & (df.estado_asignatura == 'ajustepensum'),'estado_matricula'] = 'aprobada'
#df.loc[(df.estado_matricula.isnull()) & (df.estado_asignatura == 'convalidada'),'estado_matricula'] = 'aprobada'

df = df.replace(['ajustepensum','homologada','convalidada'],'aprobada')

df = df.replace(['CALCULO I'],'CALCULO DIFERENCIAL')
df = df.replace(['ANALISI NUMERICO'],'ANALISIS NUMERICO')
df = df.replace(['DIENO DIGITAL'],'DISENO DIGITAL')
df = df.replace(['DISENO Y GESTION DE BASES DE DATOS'],'DISENO Y GESTION DE BASE DE DATOS')
df = df.replace(['ECUACIONES DIFERENCIAL'],'ECUACIONES DIFERENCIALES')
df = df.replace(['ESTRUCTURA DE DATOS OO'],'ESTRUCTURA DE DATOS ORIENTADA A OBJETOS')
df = df.replace(['FUNDAMENTOS BASICOS DE LA COMPUTACION'],'FUNDAMENTOS BASICOS DE COMPUTACION')
df = df.replace(['INGENIERIA DE SOFTWARE', 'INGENIERIA DEL SOFTWARE'],'INGENIERIA DEL SOFTWARE I')
df = df.replace(['INTELIGENCIA ARIFICIAL'],'INTELIGENCIA ARTIFICIAL')
df = df.replace(['INVESTIGACION'],'METODOLOGIA DE LA INVESTIGACION')
df = df.replace(['LENGUAJES FORMALES','LENGUAJES FORMALES Y TEORIA DE AUTOMATAS'],'AUTOMATAS Y LENGUAJES FORMALES')
df = df.replace(['MATEMATICAS','MATEMATICAS 2'],'MATEMATICAS DISCRETAS')
df = df.replace(['METODOLOGIA DE LA PROGRAMACION Y ALGORITMOS'],'METODOLOGIA DE LA PROGRAMACION')
df = df.replace(['PROGRAMACION BASICA'],'METODOLOGIA DE LA PROGRAMACION')
df = df.replace(['PROYECTOS INFORMATICOS'],'PROYECTOS INFORMATICOS I')
df = df.replace(['SIMULACIOM'],'SIMULACION')
df = df.replace(['SISTEMAS DE INFORMACION 1','SISTEMAS DE INFORMACION 2', 'SISTEMAS DE INFORMACION I','SISTEMAS DE INFORMACION II'],'SISTEMAS DE INFORMACION')
df = df.replace(['CALCULO II'],'CALCULO INTEGRAL')
df = df.replace(['FISICA','FISICA 1'],'FISICA I')
df = df.replace(['ECUACIONES DIFERENCIAL'],'ECUACIONES DIFERENCIALES')
df = df.replace(['ARQUITECTURA DE COMPUTADORES'],'ARQUITECTURA DE COMPUTADORAS')


for edad in df.fecha_nacimiento:
    #print(pd.to_datetime(edad))
    df.loc[df.fecha_nacimiento == edad,'fecha_nacimiento'] = pd.to_datetime('01/03/2020').year - pd.to_datetime(edad).year

df.drop(df.loc[(df.ciclo == 11) & (df.ciclo == 11)].index, inplace=True )
df.drop(df.loc[(df.ciclo == 12) & (df.ciclo == 12)].index, inplace=True )


df.loc[df.genero == 'femenino','genero'] = 1
df.loc[df.genero == 'masculino','genero'] = 0


df.loc[df.estado_civil.str.lower() == 'soltero(a)','estado_civil'] = 1
df.loc[df.estado_civil.str.lower() == 'casado(a)','estado_civil'] = 0
df.loc[df.estado_civil.str.lower() == 'divorciado(a)','estado_civil'] = 0

df.loc[df.etnia.str.lower() == 'mestizo','etnia'] = 1
df.loc[df.etnia.str.lower() == 'blanco','etnia'] = 2
df.loc[df.etnia.str.lower() == 'indigena','etnia'] = 3
df.loc[df.etnia.str.lower() == 'negro','etnia'] = 4
df.loc[df.etnia.str.lower() == 'mulato','etnia'] = 5
df.loc[df.etnia.str.lower() == 'montubio','etnia'] = 6


print(df.ingreso_estudiante)
print(df.columns)

df.loc[df.sector_procedencia.str.lower() == 'rural','sector_procedencia'] = 1
df.loc[df.sector_procedencia.str.lower() == 'urbano','sector_procedencia'] = 0

df.loc[df.trabaja.str.lower() == 'si','trabaja'] = 1
df.loc[df.trabaja.str.lower() == 'no','trabaja'] = 0

df.loc[df.estado_asignatura.str.lower() == 'aprobada','estado_asignatura'] = 1
df.loc[df.estado_asignatura.str.lower() == 'reprobada','estado_asignatura'] = 0


#print(df)

df.to_csv('sistemas_prueba_1.1.csv')   
