# realizado por 'Solo' a 03/05/2021



#----------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------

from config.configuration import db, coleccion

#----------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------



def coincidencia(a_buscar):
  
    datos = list(coleccion.find())
    
    for elem in datos:
        if a_buscar in elem['cita']:
            return True
    
    return False