headTest='''
<!DOCTYPE html>
<!-- Hemos añadido el atributo lang en la etiqueta html en lugar de hacerlo en meta porque el validador nos daba problemas -->
<html lang="es" dir="ltr">
    <head>
        <!-- La etiqueta meta la hemos obviado ya que en el footer hemos incluido una licencia de Creative Commons, sin embargo esta sería su sintaxis:  
        <meta name="copyright" content="Licencia de la empresa RentatorSL, propiedad de Gema Marquinez y Abel Casas"-->
        <title>Rentator</title>
        <base target="_blank">
        <meta charset="UTF-8">
        <meta name="author" content="Gema Marquinez y Abel Casas">
        <meta name="description" content="Página principal de un buscador de bicicletas para alquilar">
        <meta name="generator" content="Visual Studio Code">
        <meta name="keywords" content="Bicicletas, inicio, index, alquilar, rental, bike">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="icon" type="image/png" href="https://i.ibb.co/ZNnGXHB/favicon.jpg">
        <link rel="stylesheet" type="text/css" href="TESTfooter.css">
        <link rel="stylesheet" type="text/css" href="TESTheader.css">
        <link rel="stylesheet" type="text/css" href="TESTbase.css">
        <link rel="stylesheet" type="text/css" href="TESTnav.css">
        <link rel="stylesheet" type="text/css" href="TESTindex.css">
    </head>'''

headerTest ='''
    <body>
        <header>
            <div class="header">
                <div class="header__logo">
                    <h1>Rentator</h1>
                    <h2>Tu Mejor Opción</h2>
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
                <li><a href="index.html">Inicio</a></li>
                <li class="bicisfiltroboton">Bicicletas
                    <ul>
                        <li><a href="TESTbicis.html">Todas las bicis</a></li>
                        <li><a href="TESTbiciscategoria.html">Bicis por categoria</a></li>
                        <li><a href="TESTbicispormarca.html">Bicis por marca</a></li>
                        <li><a href="TESTbiciscaracteristica.html">Bicis por caracteristicas</a></li>
                    </ul>
                </li>
                <li><a href="TESTmarcas.html">Marcas</a></li>
                <li><a href="TESTrentals.html">Rentals</a></li>
            </ul>
        </nav>
        <div id="buscador">
                <form method="get" action="https://www.google.es/search">
                    <label for="search"></label>
                    <input type="text" id="search" placeholder="Buscar..." name="q" value="">
                </form>
        </div>
        <div  class="volverArriba">
            <a href="#nav" target="_self"><img class="flechaSubir" alt="flecha_arriba" src="http://imgfz.com/i/63T0IuS.png"></a>
        </div>'''

indexHtmlTest='''
<!DOCTYPE html>
<!-- Hemos añadido el atributo lang en la etiqueta html en lugar de hacerlo en meta porque el validador nos daba problemas -->
<html lang="es" dir="ltr">
    <head>
        <!-- La etiqueta meta la hemos obviado ya que en el footer hemos incluido una licencia de Creative Commons, sin embargo esta sería su sintaxis:  
        <meta name="copyright" content="Licencia de la empresa RentatorSL, propiedad de Gema Marquinez y Abel Casas"-->
        <title>Rentator</title>
        <base target="_blank">
        <meta charset="UTF-8">
        <meta name="author" content="Gema Marquinez y Abel Casas">
        <meta name="description" content="Página principal de un buscador de bicicletas para alquilar">
        <meta name="generator" content="Visual Studio Code">
        <meta name="keywords" content="Bicicletas, inicio, index, alquilar, rental, bike">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="icon" type="image/png" href="https://i.ibb.co/ZNnGXHB/favicon.jpg">
        <link rel="stylesheet" type="text/css" href="cssStyles/footer.css">
        <link rel="stylesheet" type="text/css" href="cssStyles/header.css">
        <link rel="stylesheet" type="text/css" href="cssStyles/base.css">
        <link rel="stylesheet" type="text/css" href="cssStyles/nav.css">
        <link rel="stylesheet" type="text/css" href="cssStyles/index.css">
    </head>
    <body>
        <header>
            <div class="header">
                <div class="header__logo">
                    <h1>Rentator</h1>
                    <h2>Tu Mejor Opción</h2>
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
                <li><a href="index.html">Inicio</a></li>
                <li class="bicisfiltroboton">Bicicletas
                    <ul>
                        <li><a href="second_pages/bicis.html">Todas las bicis</a></li>
                        <li><a href="second_pages/biciscategoria.html">Bicis por categoria</a></li>
                        <li><a href="second_pages/bicispormarca.html">Bicis por marca</a></li>
                        <li><a href="second_pages/biciscaracteristica.html">Bicis por caracteristicas</a></li>
                    </ul>
                </li>
                <li><a href="second_pages/marcas.html">Marcas</a></li>
                <li><a href="second_pages/rentals.html">Rentals</a></li>
            </ul>
        </nav>
        <div id="buscador">
                <form method="get" action="https://www.google.es/search">
                    <label for="search"></label>
                    <input type="text" id="search" placeholder="Buscar..." name="q" value="">
                </form>
        </div>
        <div  class="volverArriba">
            <a href="#nav" target="_self"><img class="flechaSubir" alt="flecha_arriba" src="http://imgfz.com/i/63T0IuS.png"></a>
        </div>
        <hr>
        <section class="contenido">
            <div class="video_background">
                <video autoplay muted loop>
                    <source src="https://thumbs-eu-west-1.myalbum.io/video/1k0_h264/8f0ee98f-a7e7-4463-9bb3-2b27b648d0c1.mp4" type='video/mp4'>
                </video>
            </div> 
            <div class="contenedorinfo" id="rutasFamosas">
                <article class="rutas">
                    <h3>Rutas mas famosas de mallorca</h3>
                    <p> Mallorca es una lugar con unos paisajes increibles, ultimamente el ciclismo se está convirtiendo en una de las formas más agradables de visitar nuestra hermosa isla. Si quieres conocer más sobre nuestro pequeño hogar, te recomendamos que visites esta página donde aparecen rutas para bicicletas y que puedas pasar un dia estupendo. ¡Estamos ansiosos por conocerte!</p>
                    
                        <div class="linkpagina"><a href="https://mallorca-touristguide.com/las-mejores-rutas-ciclistas-de-mallorca">Ir a la pagina</a></div>
                    
                </article>
            </div>
            <div class="contenedorinfo">
                <h3>Noticias mas recientes del mundo del ciclismo</h3>
                    <iframe src="https://www.esciclismo.com/actualidad/"></iframe>
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