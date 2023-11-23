import os

def clear():
  clear = "clear" if os.name == "posix" else "cls"
  os.system(clear)

