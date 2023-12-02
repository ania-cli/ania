from api import AnimeFLV
from .ui import clear, error, get_number, printb, numberf
from .utils import AnimeInfo

def select_server(animei: AnimeInfo):
  """
  Selecciona un servidor para el episodio de un anime.

  Parameters:
      animei (AnimeInfo): Información del anime y el episodio.

  Returns:
      dict: Diccionario con el servidor seleccionado y la lista completa de servidores.
  """
  clear()
  printb('Buscando servidores...')

  api = AnimeFLV()
  attempts, servers = 0, None
  while attempts <= 5:
    try:
      servers = api.get_video_servers(id=animei.id, episode=animei.episode)
      break
    except:
      attempts += 1
      continue
  
  if(servers is None):
    error(f'No se pudo cargar el episodio {animei.episode} de "{animei.title}"')

  servers = servers[0]
  
  clear()
  
  printb(f'Servidores para {animei.title} episodio {animei.episode}\n')
  for i, server in enumerate(servers):
    print(f'{numberf(i+1)} {server['title']}')
  print()

  server = get_number('Introducir numero de servidor: ', max_len=len(servers))

  print(servers[server]['server'])
  
  return dict(selected_server=servers[server], servers=servers)