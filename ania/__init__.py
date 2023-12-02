from .ui import clear, get_input
from .search_anime import search_anime
from .select_anime import select_anime
from .select_episode import select_episode

def ania():
  """
  Ejecuta la aplicación Ania para buscar y seleccionar animes.
  """
  clear()

  search = get_input('Buscar: ')
  animes = search_anime(search)
  anime = select_anime(animes, search)
  anime_info = select_episode(anime)