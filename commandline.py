#!/usr/bin/env python
#

# import modules used here -- sys is a very standard one
import sys, argparse, logging

# Gather our code in a main() function
def main(args, loglevel):
  logging.basicConfig(format="%(levelname)s: %(message)s", level=loglevel)
  
  # TODO Replace this with your actual code.
  print("executing command: runtest",args.target)
 
# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
  parser = argparse.ArgumentParser( 
                                    description = "Does a thing to some stuff.",
                                    epilog = "As an alternative to the commandline, params can be placed in a file, one per line, and specified on the commandline like '%(prog)s @params.conf'.",
                                    fromfile_prefix_chars = '@' )
  # TODO Specify your real parameters here.
  parser.add_argument("-v","--verbose",help="increase output verbosity",action="store_true")
  parser.add_argument("-t","--target",help="select a target", type=str)

  args = parser.parse_args()
  # Setup logging
  if args.verbose:
    loglevel = logging.DEBUG
  else:
    loglevel = logging.INFO
  
  main(args, loglevel)
