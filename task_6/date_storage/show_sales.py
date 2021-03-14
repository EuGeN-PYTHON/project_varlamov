from functions import show_data

def main(argv):
    program, *kwargs = argv
    show_data(*kwargs)

    return 0


if __name__ == '__main__':
   import sys

   exit(main(sys.argv))

