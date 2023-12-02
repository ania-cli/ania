from .ui import clear, get_input
from .search_anime import search_anime
from .select_anime import select_anime
from .select_episode import select_episode
from .select_server import select_server

def ania():
  """
  Ejecuta la aplicación Ania para buscar y seleccionar animes.
  """
  clear()

  search = get_input('Buscar: ')
  animes = search_anime(search)
  anime = select_anime(animes, search)
  animei = select_episode(anime)
  server = select_server(animei)

  print(server)