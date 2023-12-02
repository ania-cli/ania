from .ui import clear, printb, get_number
from termcolor import colored
from .utils import Anime

def select_anime(animes: list[Anime], search: str):
  """
  Muestra una lista de animes encontrados y permite al usuario seleccionar uno.

  Parameters:
  - animes (list[Anime]): Lista de objetos Anime que coinciden con la búsqueda.
  - search (str): Término de búsqueda utilizado para filtrar los animes.

  Returns:
  - Anime: Objeto Anime seleccionado por el usuario.
  """
  # UI
  clear()
  printb(f'Se encontraron {len(animes)} resultados para "{search}":')
  print()
  
  longest_title = len(max([anime.title for anime in animes], key=len))
  
  for i, anime in enumerate(animes):

    number = f'[{i+1}]'
    number = colored(f'{number.ljust(4)}', 'yellow')
    
    anime_title = anime.title.ljust(longest_title) 

    # UI
    print(f'{number} {anime_title} ({anime.type})')

  # UI
  print()
  anime = get_number('Introducir numero: ', max_len=len(animes))
  
  return animes[anime]
