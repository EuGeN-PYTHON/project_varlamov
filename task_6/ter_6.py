from evgeny_varlamov_HW_6 import merge_file_of_str

def main(argv):
    program, name_left, name_right, name_final = argv
    merge_file_of_str(name_left, name_right, name_final)

    return 0


if __name__ == '__main__':
   import sys

   exit(main(sys.argv))

