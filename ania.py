from ania import ania
from ania.ui import clear, printb, error, bey

if __name__ == '__main__':
    try:
        ania()

    except KeyboardInterrupt:
        bey()


#    except Exception as e:
#        error(e)