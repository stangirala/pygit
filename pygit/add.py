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
    sys.exit(41)

  # Check if file path exists
  if not os.path.exists(relative_file_path):
    sys.stderr.write('File to add does not exist.')
    sys.exit(43)

  # Check if previously tracked and so forth for other status information.

  start_cwd = os.getcwd()
  os.chdir(pygit_repo_path + '/.pygit')
  index_set = utils.read_object_from_file(globalVars.index_file_name)
  index_set.add(relative_file_path)
  utils.write_object_to_file(globalVars.index_file_name, index_set)
  os.chdir(start_cwd)

if __name__ == '__main__':
  for arg in sys.argv[1:]:
    add(arg)
