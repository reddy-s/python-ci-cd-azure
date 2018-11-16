import os
import sys

from Wrapper.wrap import Wrapper

INNER = 'INNER'
OUTER = 'OUTER'

def run(operation):
  wrapper = Wrapper()
  if operation == INNER:
    print('[INFO] {0}'.format(wrapper.call_integration_package()))
  else:
    print('[INFO] {0}'.format(wrapper.sample_wrapper_repo()))

if __name__ == "__main__":
  print("[INFO] Running Validation")
  if len(sys.argv) != 2:
    raise ValueError('[ERROR] Not enough arguments. Use "python run.py inner" or "python run.py outer"')
  if sys.argv[1].upper() not in [INNER, OUTER]:
    raise ValueError('[ERROR] The first argument has to be INNER/OUTER')
  print("[INFO] Executing program with operation: '{0}'".format(sys.argv[1].upper()))
  run(sys.argv[1].upper())
  print("[SUCCESS] Wrapping up program. Sucessfully finished execution")

