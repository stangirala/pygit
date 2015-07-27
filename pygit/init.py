import os
import sys
import errno
import utils

import globalVars

def init():
  ''' Create empty repo and other tracking data. '''

  check_if_directory_exists()
  enter_directory_and_initilize_empty_meta_data()

def check_if_directory_exists():
  try:
    os.mkdir('.pygit')
    sys.stdout.write('Creating repo.\n')
  except OSError as e:
    if e.errno == errno.EEXIST:
      sys.stdout.write('Analyzing pygit repo.\n')
      # Do nothing for now.
      pass

def enter_directory_and_initilize_empty_meta_data():
  os.chdir('.pygit')

  try:
    utils.write_object_to_file(globalVars.index_file_name, {})
    os.mkdir(globalVars.blob_object_location)
  except OSError as e:
    if e.errno == errno.ENOENT:
      sys.stderr.write('Failed to create repo.\n')

  os.chdir('../')

if __name__ == '__main__':
  init()
