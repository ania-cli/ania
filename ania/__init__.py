from animeflv import AnimeFLV
from termcolor import colored
from .ui import clear, get_input
from .utils import Anime
from .search_anime import search_anime
from .select_anime import select_anime

def ania():
  api = AnimeFLV()

  clear()

  search = get_input('Buscar: ')
  animes = search_anime(search)
  anime = select_anime(animes, search)