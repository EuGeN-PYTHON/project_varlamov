from functions import add_number


def main(argv):
    program, some_data = argv
    add_number(some_data)

    return 0


if __name__ == '__main__':
   import sys

   exit(main(sys.argv))

