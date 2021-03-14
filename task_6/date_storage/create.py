from functions import create_data

def main(argv):
    program, val, new_value = argv
    create_data(val, new_value)

    return 0


if __name__ == '__main__':
   import sys

   exit(main(sys.argv))