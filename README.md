```ruby
    /\         (_)      
   /  \   _ __  _  __ _ 
  / /\ \ | '_ \| |/ _` |
 / ____ \| | | | | (_| |
/_/    \_\_| |_|_|\__,_|
```
<!-- Badges -->
<div  styles="display: flex;">
  <img alt="Total Downlods" src="https://img.shields.io/pepy/dt/ania">
  <img alt="License" src="https://img.shields.io/pypi/l/ania">
</div>
<!-- End badges -->

Busca, disfruta y descarga anime mediante la línea de comandos en cualquier sistema operativo.

<br/>

> ⚠️ **Si estás utilizando el reproductor web**: Te recomiendo utilizar un navegador web cómo brave o firefox para evitar el tracking, anuncios y cosas molestas de los reproductores embebidos de terceros, ya que Ania no almacena el contenido de anime; este se obtiene de terceros. A la fecha solo está disponible el reproductor web local.

> PD: Estoy trabajando en el streaming desde algun reproductor de video local cómo mpv o vlc.

<br/>

**🌟 ¡No olvides darnos una estrella para que recibas notificaciones de las próximas actualizaciones!**

## Instalación

Requisitos: [python 3.8](https://www.python.org/downloads/) o superior.
```bash
pip install ania
```

Te recomiendo utilizar [pipx](https://pipx.pypa.io/) para evitar conflictos de dependencias.

```bash 
pipx install ania
```

### ¿Cómo se usa Ania? 

Despues de la instalación ejecuta el siguiente comando.

```bash
ania
```

### ¿Cómo se actualiza Ania? 

```bash
$ pip install --upgrade ania

# o puedes utilizar pipx

$ pipx upgrade ania
```

## Configurar entorno de desarrollo
Prerequisitos
+ [Python](https://www.python.org/) ^3.8
+ [Poetry](https://python-poetry.org/docs)

```bash
# Clonamos el repositorio
$ git clone https://github.com/ania-cli/ania.git

# Nos movemos al directorio 'ania'
$ cd ania

# Instalamos las dependencias
$ poetry install

# Activamos el entorno virtual
$ poetry shell

# Para ejecutar la app usamos el siguiente comando
$ poetry run ania
```

## Info para desarrolladores
### Estructura del proyecto

```ruby
.
├── ania
│   ├── api
│   │   └── __init__.py
│   ├── app.py
│   ├── get_servers.py
│   ├── __init__.py
│   ├── search_anime.py
│   ├── ui.py
│   ├── utils.py
│   └── web_player
│       ├── __init__.py
│       └── templates
│           └── index.html
├── CONTRIBUTING.md
├── LICENSE
├── poetry.lock
├── pyproject.toml
└── README.md
```

+ **./ania/**: en este directorio se encuentra todo el código de la app.

    + **api**: Aquí se encuentra una versión "custom" de [animeflv-api](https://github.com/jorgeajimenezl/animeflv-api) este modulo se encarga de hacer scraping a la web de [animeflv.net](https://animeflv.net).

    + **ui.py**: En este moduló hay métodos para interactuar con la UI, obtener inputs del usuario, limpiar la terminal, mostrar errores, etc.

    + **search_anime/**: Moduló para buscar un anime por el input dado por el usuario.

    + **select_anime/**: Moduló de UI para seleccionar un anime del listado del resultado de **search_anime.py**.

    + **select_episode/**: Moduló de UI para seleccionar un episodio del anime previamente seleccionado.

    + **get_servers.py**: Moduló para obtener los server para un episodio en específico.

    + **webplayer/**: En este moduló se encuentra el reproductor y la template para la página.

    + **webplayer/__init__.py**: En este moduló se crea el servidor web local que muestra el reproductor. 

    + **webplayer/templates/index.html**: Esta es la template para la página web, aunque sea un archivo `.html` esta usa la sintaxis de [Jinja](https://jinja.palletsprojects.com/en/3.1.x/) para que sea procesada con [Flask](https://flask.palletsprojects.com/en/3.0.x/).

    + **utils.py**: Aquí se encuentran clases para estructurar mejor algunos datos.

    + **app.py**: Aquí se ejecuta cómo tal la app haciendo uso los otros módulos de forma procedural.

## ¿Cómo Contribuir? 🤝
¡Hey! Si estás interasad@ en contribuir, reportar un bug, hacer alguna sugerencia, añadir más documentación o mejorar el código, eres bienvenid@, por favor lee 😉👉 [CONTRIBUTING.md](CONTRIBUTING.md) para más detalles. 

## Author
[@migueweb](https://github.com/migueweb)
