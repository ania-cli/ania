from ania import ania
from ania.ui import error, bye

if __name__ == '__main__':
    try:
        ania()

    except KeyboardInterrupt:
        bye()


#    except Exception as e:
#        error(e)