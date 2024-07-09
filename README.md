[Uploading Inicio.<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/css/all.min.css" integrity="sha512-KfkfwYDsLkIlwQp6LFnl8zNdLGxu9YAA1QvwINks4PhcElQSvqcyVLLD9aMhXd13uQjoXtEKNosOWaZqXgel0g==" crossorigin="anonymous" referrerpolicy="no-referrer" />
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap">
    <link rel="stylesheet" href="styles.css"/>
    <script src="script.js" defer></script>
    <title>WebTech Financial Mastery</title>
</head>
<body>
    <div class="contenido-header">
        <div id="logo">
            <img src="imagenes/_78881fc4-1efe-4915-bb51-8f76768ae06b.jpeg" alt="Logo">
        </div>
        <div id="icono-nav" class="menu-btn">
            <i class="fas fa-bars fa-2x"></i>
        </div>
        <nav id="nav" class="nav-main">
            <ul class="nav-menu">
                <li><a href="#inicio">Inicio</a></li>
                <li><a href="Nosotros\Sobre-nosotros.html">Sobre Nosotros</a></li>
                <li><a href="Servicios\Servicio.html">Servicios</a></li>
                <li><a href="Cursos\Cursos.html">Cursos</a></li>
                <li><a href="alojamiento\alojamiento.html">Alojamiento web</a></li>
                <li><a href="Contacto\Contacto.html">Contacto</a></li>
            </ul>
            <div class="redes">
                <a href="https://www.facebook.com/profile.php?id=61558466327819&sk=about" target="_blank"><i class="fa-brands fa-facebook"></i></a>
            </div>
        </nav>
    </div>
    
    <div class="presentacion-container">
        <div class="presentacion">
            <h1 class="texto-redondeado">Bienvenidos</h1>
            <br>
            <h2 class="texto-redondeado">Hola somos <strong class="texto-redondeado"> WebTech Financial Mastery</strong></h2>
            <h3 class="texto-redondeado">“Descubre el Poder de tus Finanzas y el Arte del Desarrollo Web”</h3>
            <p class="descripcion texto-redondeado">
                ¡Bienvenido a WebTech Financial Mastery! Aquí, fusionamos el conocimiento financiero con las habilidades técnicas para impulsar tu éxito. 🚀💡

¿Listo para aprender, crecer y dominar? Explora nuestros cursos, optimiza tu código y descubre oportunidades financieras. ¡Tu viaje comienza ahora!
            </p>
            <a href="https://www.facebook.com/profile.php?id=61558466327819&sk=about" target="_blank">Síguenos en Facebook</a>
        </div>
    </div>
</body>
</html>
// Función para manejar el menú responsivo
function toggleResponsiveMenu() {
    var nav = document.getElementById('nav');
    nav.classList.toggle('nav-main');
    nav.classList.toggle('responsive');
}

// Event listener para el icono de navegación responsivo
document.getElementById('icono-nav').addEventListener('click', function() {
    toggleResponsiveMenu();
});

@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');

* {
    margin: 0px;
    padding: 0px;
    box-sizing: border-box;
}

/* Estilos del cuerpo del documento */
body {
    font-family: 'Roboto', sans-serif;
    scroll-behavior: smooth;
    background-color: #d3d3d3;
    margin: 0px;
    padding: 0px;
}

.texto-redondeado {
    font-family: 'Roboto', sans-serif;
}

.contenido-header {
    background-color: rgba(0, 0, 0, 0.8);
    position: fixed;
    width: 100vw;
    z-index: 100;
    top: 0;
    left: 0px;
    margin: 0px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    height: 60px;
    padding: 20px 30px;
    flex-grow: 2;
}

#logo img {
    border-radius: 25%;
    width: 50px;
    height: 50px;
}

.nav-main {
    flex-grow: 1;
    display: flex;
    justify-content: center;
}

.nav-menu {
    list-style: none;
    display: flex;
    align-items: center;
}

.nav-menu li {
    margin: 0 15px;
}

.nav-menu li a {
    text-decoration: none;
    color: #fff;
    font-weight: bold;
    text-transform: uppercase;
    transition: color 0.3s ease;
}

.nav-menu li a:hover {
    color: #1ad5ee;
}

.redes {
  display: flex;
  align-items: center;
  justify-content: flex-end; /* Alineación a la derecha */
  margin-right: 20px; /* Espacio a la derecha */
  flex-shrink: 0; /* Evita que las redes sociales se encogan */
}

.redes a {
  text-decoration: none;
  color: #fff;
  margin-left: 10px; /* Espacio entre íconos */
  transition: color 0.3s ease;
}

.redes a:hover {
  color: #12ddef;
}

.presentacion-container {
    background: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url(imagenes/_22eedba3-5180-4087-a579-cda14da58dc2.jpeg) center center / cover;
    height: 100vh;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    color: #fff;
    text-align: center;
    position: relative;
}

.presentacion {
    max-width: 1100px;
    margin: auto;
    color: #fff;
    text-align: center;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    z-index: 2;
}

.presentacion .bienvenida {
    font-size: 16px;
    margin-bottom: 20px;
    text-transform: uppercase;
    letter-spacing: 5px;
}

.presentacion h2 {
    font-size: 20px;
    margin-bottom: 25px;
    text-align: left;
}

.presentacion h2 span {
    font-size: 25px;
    color: red;
}

.presentacion .descripcion {
    max-width: 100%;
    margin: 25px 50px;
    font-size: 18px;
    text-align: center;
}

.presentacion a {
    text-decoration: none;
    display: inline-block;
    margin: 25px 0;
    padding: 20px 25px;
    border: 2px solid #fff;
    border-radius: 50px;
    color: #fff;
    font-weight: bold;
    text-transform: uppercase;
    transition: 0.5s;
}

.presentacion a:hover {
    background-color: aqua;
}

#icono-nav {
    color: #fff;
    display: none;
    cursor: pointer;
}

/* Media queries para dispositivos móviles */
@media (max-width: 768px) {
  /* Estilos para el menú responsivo */
  #nav.responsive {
      display: block;
      background-color: rgba(0, 0, 0, 0.8);
      width: 100%; /* Ocupa todo el ancho disponible */
      height: calc(100vh - 60px); /* Calcula el alto del viewport menos la altura del header */
      position: absolute;
      top: 60px; /* Posiciona debajo del header */
      left: 0;
      padding: 10px 0;
      margin: 0;
  }

  #nav.responsive ul {
      display: block;
      text-align: center;
      height: 100%;
      display: flex;
      flex-direction: column;
      justify-content: center;
  }

  #nav.responsive ul li {
      margin: 10px 0;
      text-align: left; /* Alinea los elementos del menú a la izquierda */
  }
}


  #nav.responsive ul {
      display: block !important;
      text-align: center;
  }

  #nav.responsive ul li {
      margin: 5px 0;
      text-align: left; /* Alinea los elementos del menú a la izquierda */
  }

  @media screen and (max-width: 800px) {
    nav.responsive ul {
        display: block !important;
        text-align: center;
    }

    nav.responsive ul li {
        margin-bottom: 10px; /* Ajusta el margen inferior entre elementos */
    }
}


/* Media queries para tabletas y dispositivos móviles */
@media (max-width: 768px) {
    .nav-main {
        display: none; /* Oculta la barra de navegación en tamaños pequeños */
    }

    #icono-nav {
        display: block; /* Muestra el icono de navegación en tamaños pequeños */
    }

    .redes {
        display: none; /* Oculta las redes sociales en tamaños pequeños */
    }

    .presentacion h2 {
        font-size: 18px; /* Ajusta el tamaño del título en tamaños pequeños */
    }

    .presentacion .descripcion {
        font-size: 16px; /* Ajusta el tamaño del texto de descripción en tamaños pequeños */
    }
}

/* Media queries para dispositivos móviles */
@media (max-width: 480px) {
    .nav-main {
        display: none; /* Oculta la barra de navegación en tamaños muy pequeños */
    }

    #icono-nav {
        display: block; /* Muestra el icono de navegación en tamaños muy pequeños */
    }

    .redes {
        display: none; /* Oculta las redes sociales en tamaños muy pequeños */
    }

    .presentacion h2 {
        font-size: 16px; /* Ajusta el tamaño del título en tamaños muy pequeños */
    }

    .presentacion .descripcion {
        font-size: 14px; /* Ajusta el tamaño del texto de descripción en tamaños muy pequeños */
    }
}html…]()
