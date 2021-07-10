from utils import currency_rates

def main(argv):
   program, args = argv
   result = currency_rates(args)
   print(result)

   return 0


if __name__ == '__main__':
   import sys

   exit(main(sys.argv))




