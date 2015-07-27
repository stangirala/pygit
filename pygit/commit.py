import os

import globalVars
import utils

def commit(commit_message):
  ''' Commit current index to disk. '''
  repo_path = find_pygit_repo()

  current_index_path = repo_path + '/' + globalVars.current_index_file_name

  commit_log_path = repo_path + '/' + globalVars.commit_log

  if os.path.exists(current_index_path):
    sys.stdout.write('Nothing to commit.')
  else:
    # This should be a more interesting data structure.
    if os.path.exists(commit_log_path):
      commit_log_list = utils.read_object_from_file(commit_log_path)
    else:
      commit_log_list = []

    # do stuff with commit_log_list
    current_index_dict = utils.read_object_from_file(current_index_path)
    for filename, file_contents = current_index_dict.iteritems():
      # do nothing for now. Compute hash later
      pass

    # Get first file name are representative hash string.
    representative_hash_string = utils.compute_string_hash(current_index_dict.iteritems()[0][0])

    if not os.path.exists(globalVars.blob_object_location):
      utils.write_error_message_and_exit("Broken pygit repo. Cannot find blob objects location")
    else:
      current_commit_file_name = globalVars.blob_object_location + '/' representative_hash_string)
      utils.write_object_to_file(current_commit_file_name, current_index_dict)

    commit_log_list.append((representative_hash_string, current_commit_file_name))

    utils.write_object_to_file(commit_log_path)

    os.remove(current_index_path)
