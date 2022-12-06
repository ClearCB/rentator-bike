from src.capaPresentacion.crearHtml.funcionHtmlBase import crearHeader, crearHtmlHead, crearFooter
from src.capaNegocio.crearArchivos import crearArchivo
from src.capaDatos.listarDatosMongo import respuestaText, listarBicis
from src.capaDatos.peticionMongo import conseguirRespuestaDatos, mongoKey, mongoUrl

# En este módulo vamos a crear funciones que van a crear un archivo "bicis.html"

# En primer lugar, creamos una función que devuelva el valor del body del bicis.html
def crearBodyBicis(listaBicis):

    bicisBodyHtml ='''
        <h3 class="titleBicis"> Bicis disponibles </h3>
        <hr>
        <section>
            <div id="contenedorPadre">'''
    for bici in listaBicis:

        tipo = bici["type"]
        estado = bici["state"]
        groupset = bici["techinfo"]["groupset"]
        talla = bici["techinfo"]["size"]
        ruedas = bici["techinfo"]["wheels"]
        precio = bici["prize_euros_days"]
        complementos = bici["complements"]
        imagenBici = bici["img"]
        marca = bici["techinfo"]["brand"]
        strComplementos = ""
        for complemento in complementos:
            strComplementos += (complemento+" ")
        rental = bici["where"][0]["company_name"]

        bicisBodyHtml+=f'''
                <div class="container">
                    <div class="img">
                        <a href="./bicissolitarias/bicissolitaria{bici["_idbike"]}.html"><img src="{imagenBici}" alt="bicicleta de la marca {marca} y tipo {tipo}"></a>
                    </div>
                    <div class="contenedor_info">
                        <h5>{tipo}</h5>
                        <div class="infoBike">
                            <ul> 
                                <li>Estado: {estado}</li> 
                                <li>Marca: {marca}</li> 
                                <li>Groupset: {groupset}</li> 
                                <li>Talla: {talla}</li> 
                                <li>Tamaño de ruedas: {ruedas}</li> 
                                <li>Precio por dia: {precio}</li> 
                                <li>Complementos disponibles: {strComplementos}</li> 
                            </ul>
                        </div>
                        <div class="ubicationShow">
                            <p>Se ubica en {rental}</p>
                        </div>
                    </div>
                </div>'''
    bicisBodyHtml+='''
            </div>
        </section>'''
            

    return bicisBodyHtml

def bicisHtml(listaBicis):

    bicis=''''''
    bicis += crearHtmlHead("Bicis disponibles", "Página donde aparecen todas las bicicletas disponibles", "bicicletas, disponible, up, down alquilar, rental, bike","../cssStyles/","bicis")
    bicis += crearHeader("../","")
    bicis += crearBodyBicis(listaBicis)
    bicis += crearFooter()

    return bicis # Devolvemos la variable bicis que contiene el código del archivo bicis.html

# Definimos una función que ejecuta la función necesaria para crear el archivo correctamente.
def crearBicisHtml(listaBicis):

    crearArchivo(bicisHtml(listaBicis),".\\docs\\second_pages","bicis","html")
