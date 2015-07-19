import os
import errno
import utils

def init():
  ''' Create empty repo and other tracking data. '''

  check_if_directory_exists()
  enter_directory_and_initilize_empty_meta_data()

def check_if_directory_exists():
  try:
    os.mkdir('.pygit')
  except OSError as e:
    if e.errno == errno.EEXIST:
      print 'File exists. Analyzing pygit repo.'
      # Do nothing for now.
      pass

def enter_directory_and_initilize_empty_meta_data():
  os.chdir('.pygit')

  try:
    utils.write_object_to_file({})
  except OSError as e:
    if e.errno == errno.ENOENT:
      print 'Failed to create repo.'

  os.chdir('../')
