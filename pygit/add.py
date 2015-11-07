import os
import sys
import errno

import utils
import globalVars

def add(relative_file_path):
  try:
    pygit_repo_path = utils.find_pygit_repo()
  except utils.RepoNotFoundException:
    sys.stderr.write('Could not find pygit repo.')
    sys.exit(-1)

  index_set = utils.read_object_from_file(globalVars.index_file_name)
  index_set.add(relative_file_path)
  utils.write_object_to_file(globalVars.index_file_name, index_set)

def get_index_and_index_path(path_to_pygit_repo_index, path_to_pygit_repo_current_index):
  current_index_exists = os.path.exists(path_to_pygit_repo_current_index)

  if not current_index_exists:
    index_dict = utils.read_object_from_file(path_to_pygit_repo_index)
  else:
    index_dict = utils.read_object_from_file(path_to_pygit_repo_current_index)

  index_path = path_to_pygit_repo_current_index

  return index_dict, index_path

if __name__ == '__main__':
  for arg in sys.argv[1:]:
    add(arg)
