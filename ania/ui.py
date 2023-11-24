from termcolor import colored
import os

def clear():
  clear = "clear" if os.name == "posix" else "cls"
  os.system(clear)

def get_input(str):
  user_input = input(colored(str, 'cyan', attrs=['bold']))
  user_input = filter(None, user_input.split(' '))
  
  return ' '.join(user_input)

def error(str, clear=True ,exit=True):
  if clear:
    clear()
  print(colored(f'Error: {str}', 'red', attrs=['bold']))

  if exit:
    exit(1)

def printb (str, color='cyan'):
  print(colored(str, color, attrs=['bold']))

def get_number(str, max_len=0):
  user_input = input(colored(str, 'cyan', attrs=['bold']))
  
  if not user_input.isdigit():
    error('Debe ser un numero', clear=False, exit=False)
    return get_number(str, max_len)

  user_input = int(user_input)

  if user_input < 1 or user_input > max_len:
    error(f'Debe estar en rango de 1 a {max_len}', clear=False, exit=False)
    return get_number(str, max_len)

  return user_input - 1
