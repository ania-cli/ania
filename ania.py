from ania import ania
from ania.ui import clear, printb, error

if __name__ == '__main__':
    try:
        ania()

    except KeyboardInterrupt:
        # UI
        clear()
        printb('Regresa pronto!')
        exit(0)

#    except Exception as e:
#        error(e)