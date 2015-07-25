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
    utils.write_error_message_and_exit('Cannot find pygit repo or parent repo.')

  path_to_pygit_repo += '/.pygit/'
  path_to_pygit_repo_index = path_to_pygit_repo + '/index'

  try:
    index_dict = utils.read_object_from_file(path_to_pygit_repo_index)
    with open(filename) as file_contents:
      file_contents_hash = utils.compute_string_hash(file_contents.readlines())
    if filename in index_dict:
      sys.stdout.write('Found ' + filename + ' in index.\n')
      # Do diff etc
    else:
      sys.stdout.write('Writing ' + filename + ' contents to index.\n')
      index_dict[filename] = file_contents_hash
      utils.write_object_to_file(path_to_pygit_repo_index, index_dict)
  except OSError as e:
    if e.errno == errno.ENOENT:
      utils.write_error_message_and_exit('Failed to read index. Broken repo.')

if __name__ == '__main__':
  for arg in sys.argv[1:]:
    add(arg)
