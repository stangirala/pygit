import os
import sys
import errno

import utils
import globalVars

def get_index_and_index_path(path_to_pygit_repo_index, path_to_pygit_repo_current_index):
  current_index_exists = os.path.exists(path_to_pygit_repo_current_index)

  if not current_index_exists:
    index_dict = utils.read_object_from_file(path_to_pygit_repo_index)
  else:
    index_dict = utils.read_object_from_file(path_to_pygit_repo_current_index)

  index_path = path_to_pygit_repo_current_index

  return index_dict, index_path

def add(filename):
  ''' Main method to add files to the current index. '''

  path_to_pygit_repo = utils.find_pygit_repo()
  if path_to_pygit_repo == '':
    utils.write_error_message_and_exit('Cannot find pygit repo or parent repo.')

  path_to_pygit_repo += '/.pygit/'
  path_to_pygit_repo_index = path_to_pygit_repo + '/' + globalVars.index_file_name
  path_to_pygit_repo_current_index = path_to_pygit_repo + '/' + globalVars.current_index

  index_dict, index_path = get_index_and_index_path(path_to_pygit_repo_index, path_to_pygit_repo_current_index)

  try:
    with open(filename) as file_contents:
      file_contents = file_contents.readlines()
      if filename in index_dict:
        sys.stdout.write('Found ' + filename + ' in index.\n')
        # Do diff etc
      else:
        sys.stdout.write('Writing ' + filename + ' contents to index.\n')
        index_dict[filename] = file_contents
        utils.write_object_to_file(index_path, index_dict)
  except OSError as e:
    if e.errno == errno.ENOENT:
      utils.write_error_message_and_exit('Failed to read index. Broken repo.')

if __name__ == '__main__':
  for arg in sys.argv[1:]:
    add(arg)
