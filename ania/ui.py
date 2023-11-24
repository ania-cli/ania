from termcolor import colored
import os

def clear():
  """
  Limpia la pantalla de la terminal.

  Utiliza el comando 'clear' en sistemas tipo Unix (Linux y macOS)
  o 'cls' en sistemas Windows para limpiar la pantalla.
  """

  clear = "clear" if os.name == "posix" else "cls"
  os.system(clear)

def get_input(msg: str):
  """
  Obtiene la entrada del usuario desde la terminal.

  Args:
      msg (str): El mensaje que se muestra al usuario.

  Returns:
      str: La entrada del usuario después de eliminar espacios adicionales.
  """
  user_input = input(colored(msg, 'cyan', attrs=['bold']))
  user_input = filter(None, user_input.split(' '))
  
  return ' '.join(user_input)

def error(msg: str, clear: bool = True ,exit: bool = True):
  """
  Muestra un mensaje de error y, opcionalmente, limpia la pantalla y sale del programa.

  Args:
      msg (str): El mensaje de error.
      clear (bool): Indica si se debe limpiar la pantalla. Por defecto es True.
      exit (bool): Indica si se debe salir del programa. Por defecto es True.
  """
  if clear:
    clear()
  print(colored(f'Error: {str}', 'red', attrs=['bold']))

  if exit:
    exit(1)

def printb (msg: str, color: str ='cyan'):
  """
  Imprime un mensaje con formato en negrita y color.

  Args:
      msg (str): El mensaje a imprimir.
      color (str): El color del texto. Por defecto es 'cyan'.
  """

  print(colored(msg, color, attrs=['bold']))

def get_number(msg: str, max_len: int):
  """
  Obtiene un número del usuario dentro de un rango específico.

  Args:
      msg (str): El mensaje que indica al usuario qué ingresar.
      max_len (int): El valor máximo permitido. Por defecto es 0.

  Returns:
      int: El número ingresado por el usuario.
  """
  user_input = input(colored(msg, 'cyan', attrs=['bold']))
  
  if not user_input.isdigit():
    error('Debe ser un numero', clear=False, exit=False)
    return get_number(msg, max_len)

  user_input = int(user_input)

  if user_input < 1 or user_input > max_len:
    error(f'Debe estar en rango de 1 a {max_len}', clear=False, exit=False)
    return get_number(msg, max_len)

  return user_input - 1
