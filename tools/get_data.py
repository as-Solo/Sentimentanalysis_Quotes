# realizado por 'Solo' a 02/05/2021



#----------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------

from config.configuration import db, coleccion

#----------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------


def mensaje_autor(personaje):
    query = {"author" : f'{personaje}'}
    frases = list(collection.find(query, {"_id" : 0}))
    return frases

def mensaje_personaje():
    query = {"character_name" : 'Albus Dumbledore'}
    frases = list(collection.find(query, {"_id" : 0}))
    return frases


#-----------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------