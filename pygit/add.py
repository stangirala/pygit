import os
import sys
import errno

import utils

def find_pygit_repo():
  current_dir = os.path.abspath('./')
  while current_dir != '/':
    current_dir_ls = os.listdir(current_dir)
    if '.pygit' in current_dir_ls:
      return os.path.abspath(current_dir)

    current_dir += '/../'
    current_dir = os.path.abspath(current_dir)

  return ''

def add(filename):
  ''' Main method to add files to the current index. '''

  path_to_pygit_repo = find_pygit_repo()
  if path_to_pygit_repo == '':
    sys.stderr.write('Cannot find pygit repo or parent repo.')
    sys.exit(-1)

  path_to_pygit_repo += '/.pygit/'
  path_to_pygit_repo_index = path_to_pygit_repo + '/index'

  try:
    index_dict = utils.read_object_from_file(path_to_pygit_repo_index)
    filename_hash = utils.compute_string_hash(filename)
    if filename_hash in index_dict:
      # do something
      sys.stdout.write('Found ' + filename_hash + ' in index.\n')
      pass
    else:
      sys.stdout.write('Writing ' + filename_hash + ' to index.\n')
      index_dict[filename_hash] = filename_hash
      utils.write_object_to_file(path_to_pygit_repo_index, index_dict)
  except OSError as e:
    if e.errno == errno.ENOENT:
      print sys.stderr.write('Failed to read index. Broke repo.\n')
      sys.exit(-1)

if __name__ == '__main__':
  for arg in sys.argv[1:]:
    add(arg)
