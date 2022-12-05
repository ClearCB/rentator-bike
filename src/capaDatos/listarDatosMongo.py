# Este código va a conseguir una lista de bicis y rentals mediante la respuesta de mongoDB.

import json

# Transformar respuesta a un string
def respuestaText(respuesta):

    respuesta = respuesta.text
    respuesta = json.loads(respuesta)

    return respuesta

# Transformar respuesta a una lista de bicis
def listarBicis(respuesta):
    
    try:
        listaBicis = respuesta["documents"]
    except KeyError:
        print("El documento no cumple las condiciones de uso")
    else:
        return listaBicis

# Transformar respuesta a una lista de rentals
def listarRentals(respuesta):

    try:
        listaBicis = respuesta["documents"]
    except KeyError:
        print("El documento no cumple las condiciones de uso")
    else:
        listaRentals = []
        for bici in listaBicis:
            
            rental = bici["where"][0]

            if rental in listaRentals:
                continue
            else:
                listaRentals.append(rental)

    return listaRentals
