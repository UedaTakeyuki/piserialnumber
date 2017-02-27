import sys
import __init__ as piserialnumber

usage = 'Usage: python {} '.format(__file__)

if len(sys.argv) == 1:
  print (piserialnumber.serial())
else:
  print usage
