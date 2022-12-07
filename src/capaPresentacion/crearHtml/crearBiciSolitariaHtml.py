from src.capaNegocio.crearArchivos import crearArchivo

# Funcion que determina el html de una bici en solitario
def biciSolitariaHtml(bici):

    # Definimos parte del html de bicisolitaria
    htmlBiciSolitaria = '''
<!DOCTYPE html>
<!-- Hemos añadido el atributo lang en la etiqueta html en lugar de hacerlo en meta porque el validador nos daba problemas -->
<html lang="es" dir="ltr">
    <head>
        <!-- La etiqueta meta la hemos obviado ya que en el footer hemos incluido una licencia de Creative Commons, sin embargo esta sería su sintaxis:  
        <meta name="copyright" content="Licencia de la empresa RentatorSL, propiedad de Gema Marquinez y Abel Casas"-->
        <title>Bicis disponibles</title>
        <base target="_blank">
        <meta charset="UTF-8">
        <meta name="author" content="Gema Marquinez y Abel Casas">
        <meta name="description" content="Página donde aparece la bicicleta seleccionada y toda su informacion">
        <meta name="generator" content="Visual Studio Code">
        <meta name="keywords" content="bicicletas, disponible, up, down alquilar, rental, bike">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" type="text/css" href="../../cssStyles/footer.css">
        <link rel="stylesheet" type="text/css" href="../../cssStyles/header.css">
        <link rel="stylesheet" type="text/css" href="../../cssStyles/base.css">
        <link rel="stylesheet" type="text/css" href="../../cssStyles/nav.css">
        <link rel="stylesheet" type="text/css" href="../../cssStyles/index.css">
        <link rel="stylesheet" type="text/css" href="../../cssStyles/bicisolitaria.css">
    </head>
    <body>
        <header>
            <div class="header">
                <div class="header__logo">
                    <h1>Rentator</h1>
                    <h2>Tu Mejor Opcion</h2>
                </div>
                <div class="header__nav">
                    <div class="header__links">
                        <a href="">Iniciar Sesión</a>
                        <a href="">Registrarse</a>
                    </div>
                </div>
            </div>
        </header>
        <nav id="nav">
            <ul>
                <li><a href="../../index.html">Inicio</a></li>
                <li class="bicisfiltroboton">Bicicletas
                    <ul>
                        <li><a href="../bicis.html">Todas las bicis</a></li>
                        <li><a href="../biciscategoria.html">Bicis por categoria</a></li>
                        <li><a href="../bicispormarca.html">Bicis por marca</a></li>
                        <li><a href="../biciscaracteristica.html">Bicis por caracteristicas</a></li>
                    </ul>
                </li>
                <li><a href="../marcas.html">Marcas</a></li>
                <li><a href="../rentals.html">Rentals</a></li>
            </ul>
        </nav>
        <div id="buscador">
                <form method="get" action="https://www.google.es/search">
                    <label for="search"></label>
                    <input type="text" id="search" placeholder="Buscar..." name="q" value="">
                </form>
        </div>'''

    # Recorremos el diccionario bici para conseguir los valores que queremos
    imagen = bici["img"]
    marca = bici["techinfo"]["brand"]
    tipo = bici["type"]
    id = bici["_idbike"]
    estado = bici["state"]
    groupset = bici["techinfo"]["groupset"]
    rueda = bici["techinfo"]["wheels"]
    cuadro = bici["techinfo"]["size"]
    complementos = ""
    for complemento in bici["complements"]:
        complementos += complemento+"  "
    precio = bici["prize_euros_days"]
    ubicacion = bici["where"][0]["company_name"]

    htmlBiciSolitaria+=f'''
        <section>
            <h3 class="titleBicis">Información de la bici seleccionada</h3>
            <div class="biciinformacion">
                    <div class="img" id =img-Bike>
                        <img src="{imagen}" alt="bicicleta de la marca {marca} y catergoria {tipo}" >
                    </div>
                    <div class="descripcion">
                        <table> 
                            <tr>
                                <th>Identificador</th>
                                <th>Estado</th>
                                <th>Marca</th>
                                <th>Tipo</th>
                                <th>Groupset</th>
                                <th>Tamaño de la rueda</th>
                                <th>Tamaño del cuadro</th>
                                <th>Complementos</th>
                                <th>Precio</th>
                                <th>Ubicacion</th>
                            </tr>
                            <tr>
                                <td>{id}</td>
                                <td>{estado}</td>
                                <td>{marca}</td>
                                <td>{tipo}</td>
                                <td>{groupset}</td>
                                <td>{rueda}</td>
                                <td>{cuadro}</td>
                                <td>{complementos}</td>
                                <td>{precio}</td>
                                <td>{ubicacion}</td>
                            </tr>
                        </table>
                    </div>
            </div>
        </section>
        <footer id="footer">
            <div class="soporte_links">
                <ul>
                    <li><a href="#">Contacto: 971621612 / rentatorsl@company.eu<br><br></a></li>
                    <li><a href="#">Soporte<br><br></a></li>
                    <li>
                        <a href="https://twitter.com/topbici"><img class="icono_red" src="http://imgfz.com/i/j9If6lw.png" alt="icono de twitter" width="20" height="20"></a>
                        <a href="https://www.instagram.com/sansebikes/?hl=es"><img class="icono_red" src="http://imgfz.com/i/4YfLF68.png" alt="icono de instagram" width="20" height="20"></a>
                    </li>
                </ul>
            </div>
            <div class="copyright_footer">
                
                <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">
                    <div class="footer__license__description">
                        <p>Este obra está bajo una licencia de Creative Commons Reconocimiento-Compartir. Igual 4.0 Internacional.</p>
                    </div>

                    <div class="footer__license__img">
                        <img class="copyright_img" alt="Licencia de Creative Commons" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png">
                    </div>
                </a>
            </div>
        </footer>
    </body>
</html>'''
    return htmlBiciSolitaria


# Definimos una función que ejecuta la función necesaria para crear los archivos bicissolitarias correctamente.
def crearBiciSolitariaHtml(listaBicis):

    for bici in listaBicis: # Recorremos la lista de las bicis

        id = bici["_idbike"]
        bicisolitaria = biciSolitariaHtml(bici) # Creamos un html con los datos de la bici en concreto 
        crearArchivo(bicisolitaria,".\\docs\\second_pages\\bicissolitarias\\",f"bicissolitaria{id}","html") # Generamos un archivos html con los datos de la bici

