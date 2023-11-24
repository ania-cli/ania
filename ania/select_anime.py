from .ui import clear, printb, get_number
from termcolor import colored
from .utils import Anime

def select_anime(animes: list[Anime], search: str):
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
  
  return animes[anime].id
